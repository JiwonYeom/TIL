import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Add data to a figure by calling methods of `Axes` object. 
# FIRST argument is the X axis, second argument is the Y axis
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"])

# adding marker - o, v..
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], marker="o")

# Call the show function to show the result
plt.show()