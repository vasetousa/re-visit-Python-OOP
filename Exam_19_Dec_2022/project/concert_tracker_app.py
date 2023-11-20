from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = (
        'Guitarist',
        'Drummer',
        'Singer',
    )

    VALID_CONCERT_SKILLS = {
        'Rock': {'Drummer': ['play the drums with drumsticks'],
                 'Singer': ['sing high pitch notes'],
                 'Guitarist': ['play rock']},

        'Metal': {'Drummer': ['play the drums with drumsticks'],
                  'Singer': ['sing low pitch notes'],
                  'Guitarist': ['play metal']},

        'Jazz': {'Drummer': ['play the drums with drum brushes'],
                 'Singer': ['sing high pitch notes', 'sing low pitch notes'],
                 'Guitarist': ['play jazz']}
    }

    def __init__(self, *args):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, m_name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIAN_TYPES:
            raise ValueError('Invalid musician type!')
        searched_name = [nm for nm in self.musicians if nm.name == m_name]
        if searched_name:
            raise ValueError(f"{m_name} is already a musician!")
        mus = eval(musician_type)
        musician = mus(m_name, age)
        self.musicians.append(musician)
        return f"{m_name} is now a {musician_type}."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        music = [m for m in self.musicians if m.name == musician_name]
        band = [b for b in self.bands if b.name == band_name]
        if not music:
            raise Exception(f"{musician_name} isn't a musician!")
        elif not band:
            raise Exception(f"{band_name} isn't a band!")
        found_band = band[0]
        found_music = music[0]
        found_band.members.append(found_music)
        found_band.member_names.append(found_music.name)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        current_band = [b for b in self.bands if b.name == band_name]
        if current_band:
            c_band = current_band[0]
        else:
            raise Exception(f"{band_name} isn't a band!")
        current_musician = [m for m in self.musicians if m.name == musician_name]
        if current_musician:
            c_musician = current_musician[0]
        else:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        c_band.members.remove(c_musician)
        return f"{musician_name} was removed from {band_name}."

    def create_band(self, name: str):
        new_band = [b for b in self.bands if b.name == name]
        if new_band:
            raise Exception(f"{name} band is already created!")
        create = Band(name)
        self.bands.append(create)
        return f'{name} was created.'

    def remove_band(self, name: str):
        current_band = [b for b in self.bands if b.name == name]
        if current_band:
            band = current_band[0]
            self.bands.remove(band)
            return f'{name} was removed.'
        return f'{name} does not exist!'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        curr_concert = [c for c in self.concerts if c.place == place]
        if curr_concert:
            raise Exception(f"{place} is already registered for {genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    @staticmethod
    def check_member_skills_required_for_concert(member_skills, required_skills, member_type):
        skill_counter = 0
        required_skills_amount = len(required_skills[member_type])
        for sk in member_skills:
            if sk in required_skills[member_type]:
                skill_counter += 1
                if skill_counter >= required_skills_amount:
                    return True
        return False

    def start_concert(self, concert_place: str, band_name: str):
        valid_band_with_members = [vb for vb in self.bands if vb.name == band_name][0]  # getting the band
        members = [mem for mem in valid_band_with_members.members]  # getting the members
        members_count = len(members)
        if members_count < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        rock_counter = 0;
        metal_counter = 0;
        jazz_counter = 0
        rock_dic = ConcertTrackerApp.VALID_CONCERT_SKILLS['Rock']
        metal_dic = ConcertTrackerApp.VALID_CONCERT_SKILLS['Metal']
        jazz_dic = ConcertTrackerApp.VALID_CONCERT_SKILLS['Jazz']

        ''' check if the group can play at a Rock, Metal or Jazz concert'''
        for member in members:
            member_type = type(member).__name__
            if self.check_member_skills_required_for_concert(member.skills, rock_dic, member_type):
                rock_counter += 1
            if self.check_member_skills_required_for_concert(member.skills, metal_dic, member_type):
                metal_counter += 1
            if self.check_member_skills_required_for_concert(member.skills, jazz_dic, member_type):
                jazz_counter += 1

        results = {'Rock': rock_counter, 'Metal': metal_counter, 'Jazz': jazz_counter}
        current_concert = [con for con in self.concerts if con.place == concert_place]
        if current_concert:
            current_concert = current_concert[0]
        if results[current_concert.genre] < len(valid_band_with_members.members):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")
        profit = (current_concert.audience * current_concert.ticket_price) - current_concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {current_concert.genre} concert in {concert_place}."
