import re
str1 = "https://rr2---sn-ab5sznld.googlevideo.com/videoplayback?expire=\u0026ei=kaHtZMX3DIG48wSU6Yj4BQ\u0026ip=2604%3Aa880%3A400%3Ad0%3A0%3A0%3A1768%3A5001\u0026id=o-AN_MfkNdP4cjEEa_8bYRZcGlrnli71Y3jQ-gtIYuqrC6\u0026itag=248\u0026aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278\u0026source=youtube\u0026requiressl=yes\u0026mh=lj\u0026mm=31%2C26\u0026mn=sn-ab5sznld%2Csn-p5qs7nsk\u0026ms=au%2Conr\u0026mv=m\u0026mvi=2\u0026pl=48\u0026initcwndbps=210000\u0026siu=1\u0026spc=UWF9f75cVPmjUGvCHEesuLYn8N9xjA015SNhLzgVp1vlDpbxGIQ_Nsk\u0026vprv=1\u0026svpuc=1\u0026mime=video%2Fwebm\u0026ns=rs66cClrrZaK6uXp_kvmAc0P\u0026gir=yes\u0026clen=3982642\u0026dur=82.958\u0026lmt=1673906019552811\u0026mt=1693294623\u0026fvip=5\u0026keepalive=yes\u0026fexp=24007246%2C24363393%2C51000011\u0026c=WEB\u0026txp=5319224\u0026n=H8XU_yDmMMjzgAl0\u0026sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Csiu%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt\u0026sig=AOq0QJ8wRQIhANXpTDk7lt3ZiRBjoLthVORzJn7BVu4rr6-H_v6FGa1_AiBaqrjOE_RXdJp2OCP89T4QK60ze2pyLvMDNqapZ_Lx8Q%3D%3D\u0026lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps\u0026lsig=AG3C_xAwRQIhAL9hf00sxCC2WvG-YZj8-Oke-dULn77bPLCz4X62LrveAiBhcFBu7ypwDMj7X69SakWmOFCl74_Gvsc9HY3Frzm2ng%3D%3D"
str2 = "https://rr2---sn-ab5sznld.googlevideo.com/videoplayback?expire=1693316415&ei=36DtZMCiG4Tm8wT1o4PgBg&ip=2604%3Aa880%3A400%3Ad0%3A0%3A0%3A1768%3A5001&id=o-ADnE3aXHnAz6VgNlSTjxKcCSFWPSre5x-kb9ANrjHkRg&itag=18&source=youtube&requiressl=yes&mh=lj&mm=31%2C29&mn=sn-ab5sznld%2Csn-ab5l6nr6&ms=au%2Crdu&mv=m&mvi=2&pl=48&initcwndbps=183750&spc=UWF9fw5P4oRSCAbVG3ccfxNcynZYr2VnvfiTHXJlRg&vprv=1&svpuc=1&mime=video%2Fmp4&ns=4l76TkpM-D0oo5vDpNtSjvwP&gir=yes&clen=2860397&ratebypass=yes&dur=83.011&lmt=1673905981888642&mt=1693294391&fvip=4&fexp=24007246&beids=24350018&c=WEB&txp=5319224&n=DFsTM_bhA9E9FWCx&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAK5ccnftUFrQ0crl_hkNfC_xrOPM6tu5gaoDryivvkrtAiAZjv38w98bozYuQUHJO4R31f4Ue4x0HWcC6c5rlaMPXQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgKsOsiC0z441kyTAXQsyuLnPvnwcXlUBVWA446PhEl1ICIDyFZNvuTP5ooklHdnj-mBF9Dbt66K9o7vqHYPiXCfgi"
str1 = re.sub(r'\0026', '&', str1)
print(str1)
if str1== str2:
    print('yes')
else:
    print('no')
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i]!=str2[i]:
            print(i)
            print(str2[i:])
            break

# https://rr4---sn-ab5l6nr6.googlevideo.com/videoplayback?expire=1693298971&ei=u1ztZJz0LcSd8wTzuYmQDA&ip=2604%3Aa880%3A400%3Ad0%3A0%3A0%3A1768%3A5001&id=o-ANDCadOox2MCQYspH6eHQSgB8Sv-CcEVxaqY6ie0DWlT&itag=248&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278&source=youtube&requiressl=yes&mh=lj&mm=31%2C26&mn=sn-ab5l6nr6%2Csn-p5qlsn7s&ms=au%2Conr&mv=m&mvi=4&pl=48&initcwndbps=388750&siu=1&spc=UWF9fy0QZnEZMfJKT_SpySHxj3KOsu2xwhdbxuYu2D0gT9btNquOhHg&vprv=1&svpuc=1&mime=video%2Fwebm&ns=kiW-Xj59UsaVjNEJb9v2gjgP&gir=yes&clen=3982642&dur=82.958&lmt=1673906019552811&mt=1693277098&fvip=5&keepalive=yes&fexp=24007246%2C24363393%2C51000011&c=WEB&txp=5319224&n=