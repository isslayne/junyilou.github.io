# -*- coding:utf-8 -*-
import sys, json, urllib2, time, datetime, os, signal, exceptions

arg = signCheck = siging = brew = tti = forTime = 0; sm = nt = binvar = ""
endl = "\n"; argv = list(range(10)); masterKey = "dJ4B3uIsxyedsXeQKk_D3x"

def sig_u1(x, y): global binvar; binvar += "0"
def sig_u2(x, y): global binvar; binvar += "1"
def sig_st(x, y):
	global siging, binvar; siging = 1; binvar = ""
	print 'Received Linux siganal, analyzing.'
def sig_ed(x, y):
	global siging, arg, binvar, brew; sigans = int(binvar, 2); siging = 0
	print "Binary: " + binvar + "\nReceived new readid:", sigans
	arg += 1; brew += 1; argv[arg] = str(sigans); binvar = ""
signal.signal(signal.SIGCONT, sig_st); signal.signal(signal.SIGUSR1, sig_u1)
signal.signal(signal.SIGUSR2, sig_u2); signal.signal(signal.SIGTERM, sig_ed)

def plut(pint):
	if (pint - 1): plural = "s"
	else: plural = ""
	return plural
def blanker(bid, notice):
	blanktime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print str(os.getpid()) + " " + blanktime + " Checked " + bid + " " + notice + ", ignore."
def netTry(tryurl):
	try: response = urllib2.urlopen(tryurl)
	except urllib2.URLError: return "False"
	else: return response.read()
def pushbots(pushRaw):
	os.system("wget -t 0 -T 3 --no-check-certificate --post-data 'value1="
		+ pushRaw + "' https://maker.ifttt.com/trigger/raw/with/key/" + masterKey)
	# GitHub users please notice: IFTTT key only uses for private.
def autocomp(readid):
	aTry = netTry("https://www.kuaidi100.com/autonumber/autoComNum?text=" + readid)
	if aTry != "False":
		countp = aTry.count("comCode")
		if countp >= 2: return json.loads(aTry)["auto"][0]["comCode"]
		else: return "unknown"
	else: return "custom_network"
def home(readid):
	noShow = False; orgCounter = exsc = 0; es = ""; idt = FileLocation + '/' + readid + ".txt"; comp = "auto"; linetime = "N/A"
	if not os.path.isfile(idt): os.system("cd >" + idt); es = "[新增]"
	dtRead = open(idt); dt = dtRead.read()
	if len(dt) > 2:
		comp = dt.split(", ")[0]
		try: orgCounter = int(dt.split(", ")[1])
		except (IndexError, exceptions.ValueError): pass
		try: linetime = dt.split(", ")[2]
		except (IndexError, exceptions.ValueError): pass
	dtRead.close()
	if comp == "auto": comp = autocomp(readid)
	if comp != "unknown":
		urlb = "https://www.kuaidi100.com/query?type=" + comp + "&postid=" + readid; tryb = netTry(urlb)
		if tryb != "False":
			ansj = json.loads(tryb); today = datetime.datetime.now().strftime("%m月%d日")
			comtext = {'yuantong': '圆通', 'yunda': '韵达', 'shunfeng': '顺丰', 'shentong': '申通', 'zhongtong': '中通', 'jd': '京东'}
			if ansj["status"] == "200":
				erstat = 1; maxnum = tryb.count("location")
				if maxnum != orgCounter:
					result = ansj["data"]
					realComp = comtext.get(ansj["com"], "其他") + "快递"
					fTime = time.strftime("%-m月%-d日 %H:%M", time.strptime(result[0]["time"], "%Y-%m-%d %H:%M:%S"))
					if linetime.count(fTime) > 0: noShow = True
					reload(sys); sys.setdefaultencoding('utf-8')
					fContent = result[0]["context"].replace(" 【", "【").replace("】 ", "】").replace(" （", "（").replace(" ）", ")").replace("( ", "(").replace(" )", ")").replace('"(点击查询电话)"', "")
					signCount = fContent.count("签收") + fContent.count("感谢") + fContent.count("代收") + fContent.count("取件")
					sendCount = fContent.count("派送") + fContent.count("派件") + fContent.count("准备") + fContent.count("正在")
					if signCount > 0 and (signCount - sendCount) > 0: es = "[签收] "; exsc = maxnum;
					fileRefresh = open(idt, 'w'); fileRefresh.write(comp + ", " + str(maxnum) + ", " + fTime); fileRefresh.close()
					end = "快递查询 - " + es + realComp + " " + readid + " 新物流: " + fTime + " " + fContent
					if noShow == False: print end + endl; pushbots(end)
					else: blanker(readid, "got noShow signal")
				else: blanker(readid, "has no update")
			else:
				blanker(readid, "returned code " + ansj["status"])
				if ansj["status"] == "400": print "[" + readid + " is currently using comp code '" + comp + "'.]"
		else: blanker(readid, "failed connect")
	else:
		blanker(readid, "without company")
		print "[" + readid + " is currently using comp code '" + comp + "'.]"
	os.system("rm -f " + masterKey + "*")
	global tti; tti += 1; return exsc
for m in sys.argv[1:]: arg += 1; brew = arg
TimeInterval = 600 #10 minutes
FileLocation = os.path.expanduser('~') + "/"
for r in range (1, arg + 1): argv[r] = sys.argv[r]
print endl + "Start with PID " + str(os.getpid()) + "." + endl + "Time interval will be 10 minutes." + endl
os.system("rm -f " + FileLocation + "pid.txt&&cd >" + FileLocation + "pid.txt")
pWrite = open((FileLocation + "pid.txt"), 'w'); pWrite.write(str(os.getpid())); pWrite.close()
while True:
	if not siging:
		checkbrew = str(argv).count("-")
		for n in range(1, arg + 1): 
			readid = argv[n]
			if readid != "-": stat = home(readid)
			else: stat = 0
			if stat:
				print "Checked " + str(readid) + " signed, " + str(stat) + " updates in total recorded, refreshed " + str(tti) + " time" + plut(tti) + "."
				argv[n] = "-"; os.system("rm " + FileLocation + '/' + readid + ".txt")
		if checkbrew == brew: break
		time.sleep(TimeInterval)
	if checkbrew == brew: break
for ntm in range (0, 45): nt = nt + "="
st = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print endl + "Summary:" + endl + nt + endl + st + " All " + str(brew) + " package" + plut(brew) + " signed, exit." + endl + nt + endl
if brew > 0: pushbots("快递查询 - [退出提示] 共 " + str(brew) + " 个快递单已经被识别为签收。")