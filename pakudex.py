from pakuri import Pakuri

class Pakudex():
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakudex = []

    def get_size(self):
        return len(self.pakudex)
    def get_capacity(self):
        return self.capacity
    def check_if_full(self):
        if int(self.get_size()) == int(self.get_capacity()):
            return True
        else:
            return False
    def get_species_array(self):
        list = []
        for pakuri in self.pakudex:
            list.append(pakuri.get_species())
        return list
    def get_species_list(self):
        list = []
        counter = 0
        for pakuri in self.pakudex:
            counter += 1
            list.append(str(counter) + ". " + pakuri.get_species())

        return list

    def get_stats(self, species):
        for pakuri in self.pakudex:
            if pakuri.get_species() == species:
                return "Species: " + str(pakuri.get_species()) + "\nAttack: " + str(pakuri.get_attack()) + "\nDefense: " + str(pakuri.get_defense()) + "\nSpeed: " + str(pakuri.get_speed())

    def sort_pakuri(self):
        self.pakudex.sort(key= lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):
        if (len(self.pakudex)) < int(self.capacity):
            if species in self.get_species_array():
                return False
            else:
                self.pakudex.append(Pakuri(species))
                return True
        else:
            return False

    def evolve_species(self, species):
        if len(self.pakudex) == 0:
            return False

        for pakuri in self.pakudex:
            if species == pakuri.get_species():
                pakuri.evolve()
                return True

        return False