from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()
Sky()
cube=Entity(model="cube",color=color.green,position=(0,-100,0),collider="box",scale=5)
platform=Entity(model="cube",color=color.gray,position=(3,-100,5.7),collider="box",scale=2)
platform2=Entity(model="cube",color=color.gray,position=(3,-100,9.9),collider="box",scale=2)
platform3=Entity(model="cube",color=color.gray,position=(0,-100,13.6),collider="box",scale=2)
platform4=Entity(model="cube",color=color.gray,position=(-2,-100,17.7),collider="box",scale=2)
platform5=Entity(model="cube",color=color.gray,position=(0,-100,22),collider="box",scale=2)
platform6=Entity(model="cube",color=color.gray,position=(0,-100,26.5),collider="box",scale=2)
platform7=Entity(model="cube",color=color.azure,position=(0,-100,32),collider="box",scale=(5,1,5))
platform8=Entity(model="cube",color=color.gray,position=(-2,-100,37),collider="box",scale=2)
platform9=Entity(model="cube",color=color.gray,position=(-2,-100,41),collider="box",scale=2)
platform10=Entity(model="cube",color=color.gray,position=(0,-100,45),collider="box",scale=2)
platform11=Entity(model="cube",color=color.gray,position=(1,-100,49.5),collider="box",scale=2)
platform12=Entity(model="cube",color=color.gray,position=(0,-100,53),collider="box",scale=2)
platform13=Entity(model="cube",color=color.gray,position=(-1,-100,57.2),collider="box",scale=2)
platform14=Entity(model="cube",color=color.gray,position=(0,-100,61.2),collider="box",scale=2)
platform15=Entity(model="cube",color=color.gray,position=(1,-100,65),collider="box",scale=2)
platform16=Entity(model="cube",color=color.gray,position=(2,-100,69.3),collider="box",scale=2)
platform17=Entity(model="cube",color=color.salmon,position=(1,-100,74.5),collider="box",scale=(5,1,5))
platform18=Entity(model="cube",color=color.gray,position=(0,-100,78.3),collider="box",scale=2)
platform19=Entity(model="cube",color=color.gray,position=(0,-100,82.1),collider="box",scale=2)
platform20=Entity(model="cube",color=color.gray,position=(-1,-100,86),collider="box",scale=2)
platform21=Entity(model="cube",color=color.gold,position=(0,-100,91.2),collider="box",scale=5)



player=FirstPersonController()

app.run()
