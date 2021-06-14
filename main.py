from classRepositorio import RespositorioContactos
from classVistas import PacientsView
from controlador import ControladorPacientes
from classObjectEncoder import ObjectEncoder
def main():
    conn=ObjectEncoder('contactos.json')
    repo=RespositorioContactos(conn)
    vista=PacientsView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()