import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(right=0.75) 
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
ax.set_title('CPU and Memory usage')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Usage (%)')
cpu_line, = ax.plot([], [], label='CPU', color='#FF5733')
mem_line, = ax.plot([], [], label='Memory', color='#C70039')
ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5))

cpu_text = fig.text(0.78, 0.8, '', fontsize=10, color='#FF5733')
mem_text = fig.text(0.78, 0.75, '', fontsize=10, color='#C70039')

x_data = []
cpu_data = []
mem_data = []

def update_chart(frame):
    if frame == 0:
        return cpu_line, mem_line, cpu_text, mem_text
    
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    x_data.append(frame)
    cpu_data.append(cpu_percent)
    mem_data.append(memory_percent)

    if len(x_data) > 100:
        x_data.pop(0)
        cpu_data.pop(0)
        mem_data.pop(0)

    if x_data:
        ax.set_xlim(x_data[0], x_data[-1])

    cpu_line.set_data(x_data, cpu_data)
    mem_line.set_data(x_data, mem_data)

    cpu_text.set_text(f'CPU: {cpu_percent:.1f}%')
    mem_text.set_text(f'Memory: {memory_percent:.1f}%')

    return cpu_line, mem_line, cpu_text, mem_text

animation = FuncAnimation(fig, update_chart, interval=1000, blit=False)

for line in [cpu_line, mem_line]:
    line.set_linewidth(2)
    line.set_marker('o')
    line.set_markersize(5)

ax.set_facecolor('#F5F5F5')

plt.show()
