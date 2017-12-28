#!/usr/bin/python
# -*- coding: utf-8 -*-

import click



@click.command()
@click.option('--nand', nargs=2, type=bool)
@click.option('--nor', nargs=2, type=bool)


def unigates(nand, nor):
    if nand and not nor:
        nAND = NandGate(nand[0],nand[1]).logic()
        print(nAND)
    elif nor and not nand:
        nOR = NorGate(nor).logic()
        print(nOR)







class Gate(object):
    """ class representing a gate. It can be any gate. """

    def __init__(self, *args):
        """ initialise the class """
        self.input = args
        self.output = None

    def logic(self):
        """ the intelligence to be performed """
        raise NotImplementedError

    def output(self):
        """ the output of the gate """
        self.logic()
        return self.output


class AndGate(Gate):
    """ class representing AND gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]
        return self.output

class OrGate(Gate):
    """ class representing OR gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]
        return self.output


class NotGate(Gate):
    """ class representing NOT gate """

    def logic(self):
        self.output = not self.input[0]
        return self.output


class NandGate(AndGate,NotGate):
    #class representing Nand Gate
    
   def logic(self):
       NAND = super(NandGate,self).logic()
       Gate.__init__(self,NAND)
       self.output = NotGate.logic(self)
       return self.output

class NorGate(AndGate,NotGate):
    #class representing Nor Gate
    
   def logic(self):
       NOR = super(NorGate,self).logic()
       Gate.__init__(self,NOR)
       self.output = NotGate.logic(self)
       return self.output





if __name__ == '__main__':
    unigates()