from multiprocessing import Pool
import os

# url of the two of my backend and frontend programs
Client_Server_url = ('ExamClient/view.py', 'ExamServer/controllerFiles/controller.py')


# defining a functions that will start both processes
def execute_process(process):
    os.system('python {}'.format(process))


# staring two my process: client and server
def start_up_process():
    pool = Pool(processes=2)
    pool.map(execute_process, Client_Server_url)


if __name__ == '__main__':
    start_up_process()
