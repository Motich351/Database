from database import Client, create_session, global_init, Payment, Worker

global_init("database/db.db")
session = create_session()
clients = session.query(Client).all()
workers = session.query(Worker).all()

#Добавить клиента
#new_client = Client(fullname="Кристиан Грей", phone = "88005353536")
#session.add(new_client)
#session.commit()

#Обновить клиента


#Удалить клиента


#Показать всех клиентов
#for client in clients:
 #   #print(client.id, client.name, client.phone)
 #   print(client)
for worker in workers:
    #print(client.id, client.name, client.phone)
    print(worker)