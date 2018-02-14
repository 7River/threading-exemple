from threading import Thread
from time import sleep,clock

client_list=[]
served_client_list=[]

stop_Incoming_clients_thread=False
stop_Consumed_clients_thread=False

class Client():
    """docstring for client."""
    def __init__(self,id,start_time):
        self.id = id
        self.start_time=start_time
        self.end_time=0

    def end(self,end_time):
        self.end_time=end_time

    def get_life_span(self):
        return self.end_time-self.start_time


class Incoming_clients(Thread):
    def __init__(self,client_per_min):
        Thread.__init__(self)
        self.client_per_min=client_per_min

    def run(self):
        global client_list
        global stop_Incoming_clients_thread
        i=1
        while(not stop_Incoming_clients_thread):
            client_list.append(Client(i,clock()))
            print("client",i,"added")
            sleep(int(60/self.client_per_min))
            i+=1


class Consumed_clients(Thread):
    """docstring for Consumed_clientss."""
    def __init__(self,id,client_per_min):
        Thread.__init__(self)
        self.id=id
        self.client_per_min=client_per_min

    def run(self):
        global client_list
        global stop_Consumed_clients_thread
        while(not stop_Consumed_clients_thread):
            if(len(client_list) != 0):
                client=client_list[::-1].pop()
                client.end(clock())
                del client_list[0]
                served_client_list.append(client)
                print("client",client.id,"consumed")
                print("sleep",int(60/self.client_per_min))





#
# th_inc=Incoming_clients(60)
# th_con=Consumed_clients(1,30)
# th_con2=Consumed_clients(2,30)
# th_inc.start()
# th_con.start()
# th_con2.start()
#
#
#
# sleep(10)
# stop_Incoming_clients_thread=True
# stop_Consumed_clients_thread=True
# print([(x.id,x.get_life_span()) for x in served_client_list])

a=input()
