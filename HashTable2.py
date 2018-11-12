class HashTableNode2:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class HashTable2:

    def __init__(self, table_size):
        self.table = [None] * table_size
        self.occupied = 0


    def hash2(self, k): # converts word into a base 26 number
        key = 0
        standard = ord('a')  # since letters analyzed are lower case, will use only ASCII value 97

        for i in range(len(k)):
            base = ord(k[i]) - standard # base number determined to multiply against respective power of 26
            key += base * pow(26, (len(k) - 1 - i)) # key becomes the new, base 26 number

        return key % len(self.table)


    def insert(self, k):
        pos = self.hash2(k)
        self.table[pos] = HashTableNode2(k, self.table[pos])


    def search(self, k):
        loc = self.hash2(k)

        temp = self.table[loc]

        while temp is not None:
            if temp.item == k:
                return True
                # TODO: Two lines missing

            temp = temp.next

        return False


    def no_duplicates_insert(self, k):
        loc = self.hash2(k)

        temp = self.table[loc]

        while temp is not None:
            if temp.item == k:
                return
                        # TODO: Two Lines missing
            temp = temp.next

        self.table[loc] = HashTableNode2(k, self.table[loc])


    def get_load_factor(self):

        num_elements = 0
        for i in range(len(self.table)):
            temp = self.table[i]

            while temp is not None:
                num_elements += 1 # TODO: Replace return with body of the loop (more than 1 line missing)
                temp = temp.next
        return num_elements / len(self.table)

    def number_comparisons(self):

        total_elem = 0
        num_occupied = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            if temp is not None:
                num_occupied += 1

            while temp is not None:
                total_elem += 1
                temp = temp.next

        return total_elem/num_occupied