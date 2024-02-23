import wave
import matplotlib.pyplot as plt
import numpy as np

obj=wave.open("Output.wav","rb")        #read file , (rb) = read binary ( binary mode )
sample_freq = obj.getframerate()        #Sample frequency
n_samples=obj.getnframes()              #number of samples per time (s)
signal_wave=obj.readframes(-1)          #reading audio signal
obj.close()                             #closing the file

t_audio=n_samples / sample_freq         #duration of audio=no. of Sample/SF
print(t_audio)                          #printing the duration

#audio signal is converted to an array of integers
signal_array = np.frombuffer(signal_wave,dtype=np.int16)

# the time of array is created with start time 0 , end time equal to t_audio
times=np.linspace(0,t_audio,num=n_samples)

plt.figure(figsize=(10,5))              #new figure object ( w=10 inch , h=5 inch )
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)                     #limits of the x-axis of a plot
plt.show()
