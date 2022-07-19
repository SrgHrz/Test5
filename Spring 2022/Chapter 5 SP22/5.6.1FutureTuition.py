# Suppose that tuition for a university is $10,000 this year and
# increases by 7% every year.
# In how many years will the tuition have doubled?

year = 0  # Year 0
tuition = 10000  # OG tuition for the zeroth year

while tuition < 20000:
    year += 1
    tuition = tuition * 1.07

print("Tuition will be doubled in", year, "years.")
print("Tuition will be $" + format(tuition, ".2f"), "in", year, "years")