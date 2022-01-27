""" This package contain tuple related function"""
import logging
class tuple_parsing:
    logging.basicConfig(filename="log_file_for_tuple.log", level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")

    def __init__(self,tuples):
        self.tuples=tuples

    def is_tuple(self):
        if type(self.tuples)==tuple:
            logging.info("Given input is a tuple, input is:"+str(self.tuples))
            return 1
        else:
            logging.info("Given input is not a tuple, input is:" + str(self.tuples))
            return 0

    def Index(self, element, start=None, end=None):
            """ This function searches for a given element from the start of the tuple and
            returns the lowest index where the element appears. """
            if self.is_tuple():
                try:
                    if start != None and end == None:
                        for i in range(start, len(self.tuples)):
                            if self.tuples[i] == element:
                                logging.info("Element {} found at index: {} ".format(element, i))
                                return i
                                break
                            else:
                                logging.info("Element {} not found in range {} to {} ".format(element, start, len(self.tuples)))
                    elif start != None and end != None:
                        for i in range(start, end):
                            if self.tuples[i] == element:
                                logging.info("Element {} found at index: {} ".format(element, i))
                                return i
                                break
                            else:
                                logging.info("Element {} not found in range {} to {} ".format(element, start, end))
                    else:
                        for i in range(0, len(self.tuples)):
                            if self.tuples[i] == element:
                                logging.info("Element {} found at index: {} ".format(element, i))
                                return i
                                break
                        else:
                                logging.info("Element {} not found in the tuple ".format(element))

                except Exception as e:
                    logging.exception("some error occured" + str(e))

    def count_element(self, element):
        """This method will return the count of given element in tuple"""
        try:
            count = 0
            for i in range(len(self.tuples)):
                if self.tuples[i] == element:
                    count += 1
            logging.info("Element {} is repeated {} times is given tuple".format(element, count))
            return count
        except Exception as e:
            logging.exception("some error occured " + str(e))
            
    def sort_element(self,reverse=False):
        """ This will return sorted list"""
        try:
            tuples=list(self.tuples)
            if reverse==False:
                    for j in range(len(tuples) - 1):
                        for i in range(len(tuples) - 1):
                            if tuples[i] > tuples[i + 1]:
                                tuples[i], tuples[i + 1] = tuples[i + 1], tuples[i]
                    logging.info("Element is sucessfully sorted in ascending order and sorted tuple is : {}".format(tuple(tuples)))
                    return tuple(tuples)
            else:
                for j in range(len(tuples) - 1):
                    for i in range(len(tuples) - 1):
                        if tuples[i] < tuples[i + 1]:
                            tuples[i],tuples[i + 1] = tuples[i + 1],tuples[i]
                logging.info("Element is sucessfully sorted in Decending order and sorted tuple is : {}".format(tuple(tuples)))
                return tuple(tuples)
        except Exception as e:
            logging.error("Some error occured"+ str(e))

tup=(4,1,5,6,4,8,7,9,0,2,34,5)
x=tuple_parsing(tup)
x.sort_element(reverse=True)