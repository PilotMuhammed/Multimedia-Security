#Information Of header in Audio
import winsound
import wave
filename="AudioTest.wav"
winsound.PlaySound(filename,winsound.SND_FILENAME)
obj=wave.open(filename,"rb")
print("the number of chennel : ",obj.getnchannels())
print("the width of sample : ",obj.getsampwidth())
print("the frame rate: ",obj.getframerate())
print("the number of frames : ",obj.getnframes())
print("the params of sound ",obj.getparams())
print("the time of sound ",obj.getnframes()/obj.getframerate())
#---------------------------------------------------
#Write Audio
frames=obj.readframes(-1)
obj_new=wave.open("NewAudio.wav","wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)
obj_new.setnframes(220568)
obj_new.writeframes(frames)
winsound.PlaySound("NewAudio.wav", winsound.SND_FILENAME)
obj_new.close()