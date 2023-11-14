_DASHES = '-----------'
_PH_PER_PAGE = 4
_FAILED = 'No more free slots'
_SUCCESS = 'photo added successfully on page'


class PhotoAlbum:
    PH_PER_PAGE = _PH_PER_PAGE
    DASHES = _DASHES
    FAILED = _FAILED
    SUCCESS = _SUCCESS

    def __init__(self, pages: int):
        self.pages = pages
        self.page_index = 0
        self.photos = [[] for ph in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // cls.PH_PER_PAGE
        return cls(pages)

    def add_photo(self, label: str):
        if not self.is_space_to_add_photo():
            return self.FAILED
        self.photos[self.page_index].append(label)
        photo_added = (f"{label} {self.SUCCESS} {self.page_index + 1}"
                       f" slot {len(self.photos[self.page_index])}")
        self.go_next_page()
        return photo_added

    def go_next_page(self) -> int:
        if len(self.photos[self.page_index]) == self.PH_PER_PAGE:
            self.page_index += 1
        return self.page_index

    def is_space_to_add_photo(self) -> bool:
        aa = self.page_index < self.pages and len(self.photos[self.page_index]) < self.PH_PER_PAGE
        return aa

    def display(self):
        dash = self.DASHES




album = PhotoAlbum(2)
# print(album.photos)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)

print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.photos)
print(album.display())
