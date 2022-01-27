import logging
logging.basicConfig(filename="log_file_for_sets.log", level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

class set_parsing:

    def __init__(self,sets):
        self.sets=sets


    def is_set(self):
        if type(self.sets)==set:
            logging.info("Given Input is a set {}".format(self.sets))
            return 1
        else:
            logging.info("Given Input is not a set {}".format(self.sets))
            return 0

    def update_set(self,set1):
        """ this methis will take iterable as input and update the existing set from that"""
        try:
            if self.is_set():
                if type(set1)==set or type(set1)==list or type(set1)==tuple or type(set1)==str:
                    l1=list(self.sets)
                    l2=list(set1)
                    for i in l2:
                        l1.append(i)
                    logging.info("Updated set is {}".format(set(l1)))
                    return set(l1)
        except Exception as e:
            logging.exception("Some error occured " + str(e))

    def Add_element(self,element):
        """ This methid will add the element to the list if element is int ,str or complex else will raise ValueError"""

        try:
            if self.is_set():
                if type(element)==int or type(element)==complex or type(element)==str:
                    l1=list(self.sets)
                    l1.append(element)
                    logging.info("Element is added sucessfully. New set is : {}".format(set(l1)))
                    return set(l1)
                else:
                    raise ValueError
        except ValueError as e:
            logging.critical("unhashable type: " + str(type(element)))

    def pop_element(self):
        """ This method will remove random elements from set"""
        try:

            import random
            if self.is_set():
                l1=list(self.sets)
                random_ele=random.choice(l1)
                l1.remove(random_ele)
                logging.info("Removed element from set is {}".format(random_ele))
                return set(l1)
        except Exception as e:
            logging.info("Some error occured "+ str(e))

    def remove_elements(self,value):
        try:

            if self.is_set():
                l1=list(self.sets)
                if value not in l1:

                    raise KeyError

                else:
                    l1.remove(value)
                    logging.info("Element {} is removed sucessfully ".format(value))
                    logging.info("New set is {} ".format(set(l1)))
                    return set(l1)
        except KeyError:
            logging.error("Element {} is not present in the set".format(value))

    def intersection(self,iterable):
        try:

            if self.is_set():
                l=[]
                l1=list(self.sets)
                if type(iterable)==list or type(iterable)==tuple or type(iterable)==set or type(iterable)==str:
                    l2=list(iterable)
                else:
                    raise TypeError

                if len(l1) > len(l2):
                    for i in l1 :
                        if i in l1 and i in l2:
                            l.append(i)
                else:
                    for i in l2 :
                        if i in l1 and i in l2:
                            l.append(i)
                logging.info("Programm exceuted sucessfully!! Intersection is {}".format(set(l)))
                return set(l)
        except TypeError:
            logging.error("some error occured "+ str(e))

    def Union(self,iterable):
        """This methid will return union of set """
        try:

            if self.is_set():
                l = []
                l1 = list(self.sets)
                if type(iterable) == list or type(iterable) == tuple or type(iterable) == set or type(iterable) == str:
                    l2 = list(iterable)
                else:
                    raise TypeError
                for i in l1:
                    if i not in l:
                        l.append(i)
                for j in l2:
                    if j not in l:
                        l.append(j)
                logging.info("Programm exceuted sucessfully!! Union is {}".format(set(l)))
                return set(l)
        except TypeError:
            logging.error("some error occured " + str(e))








y=[1,2,3,4,5,8,"mkoiujhyfy","ghyu","gh"]
x=set_parsing({3,4,5,6,7,8,"ghyu"})
a=x.Union(y)
print(a)

