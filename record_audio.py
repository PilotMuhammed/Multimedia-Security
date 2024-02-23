#------ lilibraries for recording and saving audio -----
import pyaudio
import wave

#------ variables that define the audio format and quality -----
FRAME_PER_PUFFER=3200           #chunks number ( 3200 frames )
FORMAT=pyaudio.paInt16          #format of the audio samples ( 16-bitinteger format)
CHANNELS = 1                    #number of audio channels ( mono stream )
RATE = 16000                    #the sampling rate of the audio = 16000 samples per second. (Hz)

p=pyaudio.PyAudio()             #create object ( instance of PyAudio class )
#------ opens an audio stream with the specified format, channels, rate,buffer size -----
stream=p.open(
format=FORMAT,
channels=CHANNELS,
rate=RATE,
input=True,
frames_per_buffer=FRAME_PER_PUFFER
)
print("start recording")
seconds=5                       #the duration of the recording
#initializes an empty list to store the recorded audio data.
frames=[]
#("' The for loop records audio data in chunks of size FRAME_PER_PUFFER"
#"for a total of 5 seconds and appends each chunk to the frames list.'")
for i in range(0,int(RATE/FRAME_PER_PUFFER*seconds)):
    data=stream.read(FRAME_PER_PUFFER)
    frames.append(data)

stream.stop_stream()        #stop the audio stream
stream.close()              #close the audio stream
p.terminate()               #terminate the PyAudio instance

#create a new WAV file named “Output.wav” in write mode
obj=wave.open("x.wav","wb")
obj.setnchannels(CHANNELS) #set the number of channels in the WAV file to 1
obj.setsampwidth(p.get_sample_size(FORMAT)) #set the sample width in bytes based on the specified format
obj.setframerate(RATE) #set the frame rate of the WAV file to 16000 frames per second
obj.writeframes(b"".join(frames)) #write the recorded audio data to the WAV file
obj.close()
#close the WAV file object