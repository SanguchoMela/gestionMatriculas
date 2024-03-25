from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def login(self):
        self.client.post("/api/login",json={"email":"melany@hotmail.com","password":"1234"})
        self.client.get("/api/usuario/65fdfcd3dc36dc44026dbf48")
        self.client.get("/api/estudiante/65efe229ecc948a852dc787b")
        self.client.get("/api/materia/65ed5791eba55fa46b263bae")
        self.client.get("/api/matricula/65edefbdb67c6a77ca273e4a")