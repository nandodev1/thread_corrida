#/bin/bash python3

from threading import Thread, Semaphore
from sys import stdout, stdin
from time import sleep
import logging
import time
import random

global semaforo
semaforo = Semaphore(0)

global out
out = None 
global en
en = 0
bufferDeInprecao = [None] * 10

global arq_conp
arq_conp = open('arq_conp.txt')

class Sub_proc(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
        self.entrada = 0
    def run(self):
        enviou_arq = False
        stdout.write( self.name + ' Foi iniciado!\n')
        if self.id == 'C':
            sleep(1)
        while(True):
            #semaforo.acquire(self)
            if enviou_arq == False:
                global en
                self.entrada = en
                bufferDeInprecao[self.entrada] = self.id
                stdout.write( self.name + ' enviou arquivo ' + self.id 
                             + ' para impreção!\n'
                             )
                print('        ', bufferDeInprecao)
                stdout.flush()
                stdout.write(  self.name 
                        + ' Entrada: ' 
                        + str(self.entrada)
                        + ' Arquivo: '
                        + self.id + '\n')
                stdout.flush()
                if en > 9:
                    en = 0
                else:
                    en += 1
                stdout.write(  self.name + ' Somou indice de entrada!\n')
                stdout.flush()
                enviou_arq = True
            #semaforo.release(self)

def main():
    threads = []
    for id in ['A', 'B', 'C', 'D', 'E']:
        sub_proc = Sub_proc(id)
        threads.append(sub_proc)
        stdout.write(  sub_proc.name + ' Foi criado!\n')
        stdout.flush()
    for sub_proc in threads:
        sub_proc.start()
        stdout.flush()
    while(en == 5):
        print(bufferDeInprecao)
        exit(0)


if __name__ == "__main__":
    main()