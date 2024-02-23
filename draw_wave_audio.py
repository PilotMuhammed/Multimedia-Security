#Draw Wave Of Audio
import wave
from matplotlib import pyplot as plt
import numpy as nb
obj=wave.open("AudioTest.wav","rb")
sample_frq=obj.getframerate()
n_sample=obj.getnframes()
signal_wave=obj.readframes(-1)
obj.close()
t_audio=n_sample/sample_frq
print(t_audio)
signal_arr=nb.frombuffer(signal_wave,dtype=nb.int16)
time=nb.linspace(0,t_audio,num=n_sample)
plt.figure(figsize=(15,5))
plt.plot(time,signal_arr)
plt.title("Audio signal")

plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0,t_audio)
plt.show()
