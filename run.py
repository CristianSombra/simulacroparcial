from app import create_app, db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)



# from app import create_app, db
# from app.models import Persona

# app = create_app()

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#         persona1 = Persona(
#             nombre="Cristian",
#             edad=35,
#             email="cristiansombra87@gmail.com",
#             foto_url="https://github.com/CristianSombra"
#         )
#         db.session.add(persona1)
#         db.session.commit()
#         print("Persona1 creada correctamente")
    
#     app.run(debug=False)