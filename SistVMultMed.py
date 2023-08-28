class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):

        self.__lista_caninos = []
        self.__lista_felinos = []
    
    def verificarExiste(self,historia,tipo):
        if tipo == 1:
            for m in self.__lista_felinos:            
                if historia == m.verHistoria():
                    return True
        if tipo == 2:
            for m in self.__lista_caninos:            
                if historia == m.verHistoria():
                    return True
                
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self,tipo):
        if tipo == 1:
            return  len(self.__lista_caninos)

        if tipo == 2:    
            return len(self.__lista_felinos)
    
    def ingresarMascota(self,mascota,tipo):

        if tipo == 1:
            self.__lista_felinos.append(mascota) 
        if tipo == 2:
            self.__lista_caninos.append(mascota)
   

    def verFechaIngreso(self,historia,tipo):
        #busco la mascota y devuelvo el atributo solicitado
        if tipo == 1:
            for masc in self.__lista_felinos:
                if historia == masc.verHistoria():
                    return masc.verFecha() 
            return None
        
        if tipo == 2:
            for masc in self.__lista_caninos:
                if historia == masc.verHistoria():
                    return masc.verFecha() 
            return None

    def verMedicamento(self,historia,tipo):
        #busco la mascota y devuelvo el atributo solicitado
        if tipo == 1:
            for masc in self.__lista_felinos:
                if historia == masc.verHistoria():
                    return masc.verLista_Medicamentos() 
            return None
        
        if tipo == 2:
            for masc in self.__lista_caninos:
                if historia == masc.verHistoria():
                    return masc.verLista_Medicamentos() 
            return None
    
    def eliminarMascota(self, historia,tipo):
        if tipo == 1:
            for masc in self.__lista_felinos:
                if historia == masc.verHistoria():
                    self.__lista_felinos.remove(masc)  #opcion con el pop
                    return True  #eliminado con exito
            return False 
        
        if tipo == 2:
            for masc in self.__lista_caninos:
                if historia == masc.verHistoria():
                    self.__lista_caninos.remove(masc)  #opcion con el pop
                    return True  #eliminado con exito
            return False 
    

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 

            while True:
                    try:
                        tipo=int(input("Ingrese el tipo de mascota \n\n1. felino \n2. canino \n"))
                        while tipo !=1 and tipo != 2:
                                print("la variable ingresada no es valida, por favor ingrese nuevamente")
                                int(tipo=input("Ingrese el tipo de mascota (felino o canino): "))
                        break  
                    except:
                        print("PARAMETRO INVALIDO")

            if servicio_hospitalario.verNumeroMascotas(tipo) >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia,tipo) == False:
                nombre=input("Ingrese el nombre de la mascota: ")

                peso=int(input("Ingrese el peso de la mascota: "))
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))

                lista_med=[]
                lista_med2=[]
                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis =int(input("Ingrese la dosis: "))
                    for p in lista_med2: 

                        if nombre_medicamentos == p:
                            print("Este medicamento ya se encuentra registrado, por favor ingrese uno nuevo")
                            nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    lista_med2.append(nombre_medicamentos)       
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                        

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas,tipo)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            while True:
                    try:
                        tipo=int(input("Ingrese el tipo de mascota \n\n 1. felino \n2. canino \n"))
                        while tipo !=1 and tipo != 2:
                                print("la variable ingresada no es valida, por favor ingrese nuevamente")
                                int(tipo=input("Ingrese el tipo de mascota (felino o canino): "))
                        break  
                    except:
                        print("PARAMETRO INVALIDO")

            fecha = servicio_hospitalario.verFechaIngreso(q,tipo)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            while True:
                    try:
                        tipo=int(input("Ingrese el tipo de mascota \n\n 1. felino \n2. canino \n"))
                        while tipo !=1 and tipo != 2:
                                print("la variable ingresada no es valida, por favor ingrese nuevamente")
                                int(tipo=input("Ingrese el tipo de mascota (felino o canino): "))
                        break  
                    except:
                        print("PARAMETRO INVALIDO")
            numero=servicio_hospitalario.verNumeroMascotas(tipo)
            print("El número de pacientes en el sistema son: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            while True:
                    try:
                        tipo=int(input("Ingrese el tipo de mascota \n\n 1. felino \n2. canino \n"))
                        while tipo !=1 and tipo != 2:
                                print("la variable ingresada no es valida, por favor ingrese nuevamente")
                                int(tipo=input("Ingrese el tipo de mascota (felino o canino): "))
                        break  
                    except:
                        print("PARAMETRO INVALIDO")
            medicamento = servicio_hospitalario.verMedicamento(q,tipo) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            while True:
                    try:
                        tipo=int(input("Ingrese el tipo de mascota \n\n 1. felino \n2. canino \n"))
                        while tipo !=1 and tipo != 2:
                                print("la variable ingresada no es valida, por favor ingrese nuevamente")
                                int(tipo=input("Ingrese el tipo de mascota (felino o canino): "))
                        break  
                    except:
                        print("PARAMETRO INVALIDO")
            resultado_operacion = servicio_hospitalario.eliminarMascota(q,tipo) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

