from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project.teams.base_team import BaseTeam
from project.equipment.base_equipment import BaseEquipment


class Tournament:
    VALID_EQUIPMENT = ("KneePad", "ElbowPad")
    VALID_TEAMS = ("OutdoorTeam", "IndoorTeam")

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError('Tournament name should contain letters and digits only!')
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in Tournament.VALID_EQUIPMENT:
            raise Exception('Invalid equipment type!')

        obj = eval(equipment_type)
        new_equipment = obj(0, 0)
        self.equipment.append(new_equipment)
        return f'{equipment_type} was successfully added.'

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in Tournament.VALID_TEAMS:
            raise Exception('Invalid team type!')

        elif self.capacity <= 0:
            return 'Not enough tournament capacity.'

        obj = eval(team_type)
        team_name_check = [tt for tt in self.teams if tt.name == team_name]
        if not team_name_check:
            new_team = obj(team_name, country, advantage)
            self.teams.append(new_team)
            self.capacity -= 1
            return f'{team_type} was successfully added.'
        return f'Team {team_name} was already added.'

    def sell_equipment(self, equipment_type: str, team_name: str):
        eq_availability = [eq for eq in self.equipment if str(eq.__class__.__name__) == equipment_type]
        if eq_availability:
            equipment = eval(equipment_type)
            list_index = 0

            for index, value in enumerate(self.equipment):
                if str(value.__class__.__name__) == equipment_type:
                    equipment = value
                    list_index = index

            team = [te for te in self.teams if te.name == team_name][0]
            if team.budget < equipment.price:
                raise Exception('Budget is not enough!')
            if equipment:
                team.equipment.append(equipment)
                team.budget -= equipment.price
                del self.equipment[list_index]
                return f'Successfully sold {equipment_type} to {team_name}.'
        return f'No more {equipment_type} equipment in the inventory.'

    def remove_team(self, team_name: str):
        team = [te for te in self.teams if te.name == team_name]
        if not team:
            raise Exception('No such team!')
        team = team[0]
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        self.capacity += 1
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment = [eq.increase_price() for eq in self.equipment if str(eq.__class__.__name__) == equipment_type]

        return f'Successfully changed {len(equipment)}pcs of equipment.'

    def play(self, team_name1: str, team_name2: str):
        team1 = [t for t in self.teams if t.name == team_name1]
        team2 = [t for t in self.teams if t.name == team_name2]
        team1 = team1[0]
        team2 = team2[0]
        if str(team1.__class__.__name__) != str(team2.__class__.__name__):
            raise Exception('Game cannot start! Team types mismatch!')
        eq1 = 0
        eq2 = 0
        for el1 in team1.equipment:
            eq1 += el1.protection
        for el2 in team2.equipment:
            eq2 += el2.protection
        points1 = team1.advantage + eq1
        points2 = team2.advantage + eq2

        if points1 > points2:
            team1.win()
            return f"The winner is {team_name1}."
        elif points1 < points2:
            team2.win()
            return f"The winner is {team_name2}."
        else:
            return 'No winner in this game.'

    def get_statistics(self):
        teams = [te.get_statistics() for te in self.teams]

        return f'Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:\n{"\n".join(teams)}\n'