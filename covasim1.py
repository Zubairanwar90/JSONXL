import covasim as cv
# Define a custom intervention
def elderly(sim, old=70):
    if sim.t == sim.day('2020-04-01'):
        elderly = sim.people.age > old
        sim.people.rel_sus[elderly] = 0.0
# Set custom parameters
pars = dict(
    pop_type = 'hybrid', # More realistic population
    location = 'japan', # Japan's population pyramid
    pop_size = 50e3, # Have 50,000 people total
    pop_infected = 100, # 100 infected people
    n_days = 90, # Run for 90 days
)
# Run multiple sims in parallel and plot key results
label = 'Protect the elderly'
s1 = cv.Sim(pars, label='Default')
s2 = cv.Sim(pars, interventions=elderly, label=label)
msim = cv.parallel(s1, s2)
msim.plot(['cum_deaths', 'cum_infections'])