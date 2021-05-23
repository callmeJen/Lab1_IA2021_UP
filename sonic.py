import retro

env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

env.reset()

done = False

while not done:
    env.render()

    action = env.action_space.sample()
    ob, rew, done, info = env.step(action)
    print("Action ", action, "Reward ", rew)

with open('sonic-data-'+ unique_filename +'.csv', 'a', newline='') as file:
writer = csv.writer(file)
writer.writerow(["B", "A", "MODE", "START", "UP", "DOWN", "LEFT", "RIGHT", "C", "Y", "X", "Z"])
writer.writerow(action)
    print("Action ", action, "Reward ", rew)