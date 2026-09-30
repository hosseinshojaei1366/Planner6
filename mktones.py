import wave,struct,math
T={'bell':[(880,.35),(1320,.5)],'chime':[(660,.2),(880,.2),(1100,.4)],'beep':[(1000,.15),(0,.1),(1000,.15),(0,.1),(1000,.15)],'alarm':[(900,.3),(700,.3)]*3}
R=22050
for n,seg in T.items():
    fr=[]
    for f,d in seg:
        N=int(R*d)
        for i in range(N):
            e=min(1,i/300,(N-i)/300)
            fr.append(struct.pack('<h',0 if f==0 else int(9000*e*math.sin(2*math.pi*f*i/R))))
    w=wave.open('tone_%s.wav'%n,'wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(R);w.writeframes(b''.join(fr));w.close()
