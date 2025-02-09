class Page:
    def __init__(self, name, next_pages):
        self.name = name
        self.next_pages = next_pages

# Define pages and navigation
home = Page("Home", ["Create New List", "View Existing List", "Settings"])
new_list = Page("Create New List", ["Add Items", "Home"])
add_items = Page("Add Items", ["Edit List", "Home"])
edit_list = Page("Edit List", ["Home"])
settings = Page("Settings", ["Home"])

# Store pages
pages = [home, new_list, add_items, edit_list, settings]

# Print page details
print(f"Total Pages: {len(pages)}\n")
for page in pages:
    print(f"Page: {page.name}")
    print(f"Next: {', '.join(page.next_pages)}\n")
