import subprocess,os,json,sys
SC="/tmp/claude-0/-home-user-a1/fddcc687-8f8b-5481-834b-8050c52e2545/scratchpad"
V=f"{SC}/chr/vid"; VO=f"{SC}/voice"; OUT=f"{SC}/rough"; os.makedirs(OUT,exist_ok=True)
SEQ={
"SQ01":["SH001","SH002","SH003","SH004","SH005"],
"SQ02":["SH001","SH002","SH003","SH004","SH005","SH006"],
"SQ03":["SH001","SH002","SH003","SH004","SH005","SH006A","SH006B","SH006C"],
"SQ04":["SH001","SH002","SH003","SH004","SH005","SH006","SH007"],
"SQ05":["SH001","SH002","SH003"],
"SQ06":["SH001","SH002","SH003","SH004","SH005","SH006","SH007"],
"SQ07":["SH001","SH002","SH003","SH004","SH005","SH006","SH007"],
"SQ08":["SH001","SH002","SH002I","SH003","SH004","SH005","SH006","SH007","SH008","SH009","SH010"],
}
VOS={("SQ01","SH001"):("EP01_VO01_take1",1.5),("SQ02","SH006"):("EP01_VO02_take1",0.2),("SQ03","SH003"):("EP01_VO03_take1",2.0),("SQ04","SH001"):("EP01_VO04_take1",2.0),("SQ05","SH003"):("EP01_VO05_take1",1.0)}
def clip(sq,sh):
    for v in ("v3","v2","v1"):
        p=f"{V}/EP01_{sq}_{sh}_MOTION_GROK_{v}.mp4"
        if os.path.exists(p): return p
    raise SystemExit("missing "+sq+sh)
def dur(p): return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p]).decode())
listing=[]
for sq,shots in SEQ.items():
    parts=[]
    for sh in shots:
        src=clip(sq,sh); o=f"{OUT}/{sq}_{sh}.mp4"
        cmd=["ffmpeg","-v","error","-y","-i",src]
        if (sq,sh) in VOS:
            n,off=VOS[(sq,sh)]
            cmd+=["-i",f"{VO}/{n}.mp3","-filter_complex",f"[0:a]volume=0.35[g];[1:a]adelay={int(off*1000)}|{int(off*1000)},volume=1.6[n];[g][n]amix=inputs=2:duration=first:normalize=0[a];[0:v]scale=1280:720,fps=30,setsar=1[v]","-map","[v]","-map","[a]"]
        else:
            cmd+=["-filter_complex","[0:a]volume=1.0[a];[0:v]scale=1280:720,fps=30,setsar=1[v]","-map","[v]","-map","[a]"]
        cmd+=["-c:v","libx264","-crf","26","-preset","veryfast","-c:a","aac","-ar","48000","-ac","2","-b:a","128k",o]
        subprocess.run(cmd,check=True); parts.append(o)
    lst=f"{OUT}/{sq}.txt"; open(lst,"w").write("".join(f"file '{p}'\n" for p in parts))
    out=f"{OUT}/EP01_{sq}_ROUGHCUT_v1.mp4"
    subprocess.run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",lst,"-c","copy",out],check=True)
    listing.append(out); print(sq, round(dur(out),1),"s", round(os.path.getsize(out)/1e6,1),"MB",flush=True)
open(f"{OUT}/all.txt","w").write("".join(f"file '{p}'\n" for p in listing))
subprocess.run(["ffmpeg","-v","error","-y","-f","concat","-safe","0","-i",f"{OUT}/all.txt","-c","copy",f"{OUT}/EP01_FULL_ROUGHCUT_v1.mp4"],check=True)
f=f"{OUT}/EP01_FULL_ROUGHCUT_v1.mp4"; print("FULL",round(dur(f),1),"s",round(os.path.getsize(f)/1e6,1),"MB")
