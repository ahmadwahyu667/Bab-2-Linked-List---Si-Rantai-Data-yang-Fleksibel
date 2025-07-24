class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        print("Isi Playlist:")
        current_node = self.head
        if current_node is None:
            print("(Playlist kosong)")
            return
        while current_node is not None:
            print(f"- {current_node.data}")
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"Error: Data '{key}' tidak ditemukan.")
            return
        prev.next = current_node.next
        current_node = None

    def insert_after(self, prev_node_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node = Node(new_data)
                new_node.next = current_node.next
                current_node.next = new_node
                print(f"Sukses: '{new_data}' disisipkan setelah '{prev_node_data}'")
                return
            current_node = current_node.next
        print(f"Error: Data pendahulu '{prev_node_data}' tidak ditemukan.")

playlist = LinkedList()
playlist.append("Lagu Pop - A")
playlist.append("Lagu Rock - B")
playlist.append("Lagu Jazz - C")
playlist.print_list()

print("\nMenambah lagu intro...")
playlist.prepend("Intro Musik")
playlist.print_list()

print("\nMenyisipkan 'Lagu Iklan' setelah 'Intro Musik'...")
playlist.insert_after("Intro Musik", "Lagu Iklan")
playlist.print_list()

print("\nMenghapus 'Lagu Rock - B'...")
playlist.delete_node("Lagu Rock - B")
playlist.print_list()

print("\nMencoba menghapus lagu yang salah...")
playlist.delete_node("Lagu Dangdut")
playlist.print_list()

print("\nMenambah lagu penutup...")
playlist.append("Outro Musik")
playlist.print_list()

print("\nMembuat playlist baru dan mengeceknya...")
playlist_kosong = LinkedList()
playlist_kosong.print_list()