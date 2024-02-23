# Encrypt and decrypt audio

#Fernet is a symmetric key encryption system
from cryptography.fernet import Fernet
import wave

#key is a random 256-bit (32-byte)
def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename):
    return open(filename, 'rb').read()

def encrypt_audio(audio_path, output_path, key):
    cipher = Fernet(key)
    # Open the audio file
    audio = wave.open(audio_path, 'rb')
    frames = audio.readframes(audio.getnframes())
    # Encrypt audio data
    encrypted_frames = cipher.encrypt(frames)
    # Create a new wave file with encrypted data
    output_audio = wave.open(output_path, 'wb')
    output_audio.setparams(audio.getparams())
    output_audio.writeframes(encrypted_frames)

    # Close the files
    audio.close()
    output_audio.close()

def decrypt_audio(encrypted_path, output_path, key):
    cipher = Fernet(key)

    # Open the encrypted audio file
    encrypted_audio = wave.open(encrypted_path, 'rb')
    encrypted_frames = encrypted_audio.readframes(encrypted_audio.getnframes())

    # Decrypt audio data
    decrypted_frames = cipher.decrypt(encrypted_frames)

    # Create a new wave file with decrypted data
    output_audio = wave.open(output_path, 'wb')
    output_audio.setparams(encrypted_audio.getparams())
    output_audio.writeframes(decrypted_frames)
    # Close the files
    encrypted_audio.close()
    output_audio.close()

# Example usage:
audio_path = 'enc.wav'
encrypted_path = 'encrypted_audio.wav'
decrypted_path = 'decrypted_audio.wav'

# Generate and save encryption key
key = generate_key()
save_key(key, 'encryption_key.key')

# Encrypt audio
encrypt_audio(audio_path, encrypted_path, key)

# Decrypt audio
decrypt_audio(encrypted_path, decrypted_path, key)