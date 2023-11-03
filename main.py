#/bin/bash python3

from threading import Thread, Semaphore
from sys import stdout, stdin
from time import sleep
import logging
import time
import random

global semaforo
semaforo = Semaphore(1)

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
        if self.id == 'A':
            sleep(1)
        if self.id == 'B':
            sleep(1)
        if self.id == 'C':
            sleep(1)
        if self.id == 'D':
            sleep(1)
        if self.id == 'E':
            sleep(1)
        while(enviou_arq == False):
            #semaforo.acquire()
            #print( '        ', self.name, ' Esta usando recurso compartilhado')
            if enviou_arq == False:
                global en
                self.entrada = en
                bufferDeInprecao[self.entrada] = self.id
                stdout.write(  self.name 
                        + ' Slot: ' 
                        + str(self.entrada)
                        + ' Arquivo: '
                        + self.id + '\n')
                stdout.flush()
                stdout.write( self.name + ' enviou arquivo ' + self.id 
                             + ' para impresão!\n'
                             )
                print('        ', bufferDeInprecao)
                stdout.flush()
                if en > 9:
                    en = 0
                else:
                    en += 1
                stdout.write(  self.name + ' Somou indice de entrada!\n'
                + '         Próximo slot livre: ' + str(en) +'\n')
                stdout.flush()
                enviou_arq = True
            #semaforo.release()
            #print( '        ', self.name, ' Liberou o recurso compartilhado')

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


if __name__ == "__main__":
    main()
