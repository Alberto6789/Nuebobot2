from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<20):
			if porcent >= index_make * 5: make_text+= '✦'
			else: make_text+= '✧'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '📥𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐📡... \n\n'
    msg+= '🏷️ 𝙽𝚊𝚖𝚎: ' + str(filename)+'\n'
    msg+= '📦 𝚃𝚘𝚝𝚊𝚕 𝚜𝚒𝚣𝚎: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚍: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📶 𝚂𝚙𝚎𝚎𝚍: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '⏲️ 𝚃𝚒𝚖𝚎 𝚕𝚎𝚏𝚝: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = '📥𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚏𝚒𝚕𝚎📡...\n\n'
    msg += '📦 𝙵𝚒𝚕𝚎: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '📊 𝙿𝚎𝚛𝚌𝚎𝚗𝚝𝚊𝚐𝚎: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += '📦 𝚃𝚘𝚝𝚊𝚕 𝚜𝚒𝚣𝚎: '+sizeof_fmt(totalBits)+'\n\n'
    msg += '📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚍: '+sizeof_fmt(currentBits)+'\n\n'
    msg += '📶 𝚂𝚙𝚎𝚎𝚍: '+sizeof_fmt(speed)+'/s\n\n'
    msg += '⏲️ 𝚃𝚒𝚖𝚎 𝚕𝚎𝚏𝚝: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '📤𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐☁️... \n\n'
    msg+= '🏷️ 𝙵𝚒𝚕𝚎: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📤𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐: ' + str(filename)+'\n'
    msg+= '📦 𝚃𝚘𝚝𝚊𝚕 𝚜𝚒𝚣𝚎: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '📤 𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '📶 𝚂𝚙𝚎𝚎𝚍: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '⏲️ 𝚃𝚒𝚖𝚎 𝚕𝚎𝚏𝚝: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = '📤𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐☁️...\n\n'
    msg += '🏷️ 𝙽𝚊𝚖𝚎: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📚 𝙿𝚊𝚛𝚝: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '📊 𝙿𝚎𝚛𝚌𝚎𝚗𝚝𝚊𝚐𝚎: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += '📦 𝚃𝚘𝚝𝚊𝚕 𝚜𝚒𝚣𝚎: '+sizeof_fmt(totalBits)+'\n\n'
    msg += '📤 𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍: '+sizeof_fmt(currentBits)+'\n\n'
    msg += '📶 𝚂𝚙𝚎𝚎𝚍: '+sizeof_fmt(speed)+'/s\n\n'
    msg += '⏲️ 𝚃𝚒𝚖𝚎 𝚕𝚎𝚏𝚝: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '🗜️𝙲𝚘𝚖𝚙𝚛𝚎𝚜𝚜𝚒𝚗𝚐🗜️... \n\n'
    msg+= '🏷️ 𝙽𝚊𝚖𝚎: ' + str(filename)+'\n'
    msg+= '📦 𝚃𝚘𝚝𝚊𝚕 𝚜𝚒𝚣𝚎: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📚 𝙿𝚊𝚛𝚝𝚜 𝚜𝚒𝚣𝚎: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '📕 𝙰𝚖𝚘𝚞𝚗𝚝 𝚘𝚏 𝚙𝚊𝚛𝚝𝚜: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'

    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '📌𝙵𝚒𝚗𝚒𝚜𝚑𝚎𝚍 𝚙𝚛𝚘𝚌𝚎𝚜𝚜📌\n\n'
    msg+= '🏷️ 𝙽𝚊𝚖𝚎: ' + str(filename)+'\n'
    msg+= '📦 𝚃𝚘𝚝𝚊𝚕 𝚜𝚒𝚣𝚎: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📚 𝙿𝚊𝚛𝚝𝚜 𝚜𝚒𝚣𝚎: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= '📤 𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝚙𝚊𝚛𝚝𝚜: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= '🗑️𝙳𝚎𝚕𝚎𝚝𝚎 𝚏𝚒𝚕𝚎🗑️: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🔗𝙻𝚒𝚗𝚔𝚜🔗</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">🔗' + f['name'] + '🔗</a>'
            msg+= "<a href='"+url+"'>🔗"+f['name']+'🔗</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '📑𝙵𝚒𝚕𝚎𝚜 ('+str(len(evfiles))+')📑\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '⚙️𝚄𝚜𝚎𝚛 𝚌𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚊𝚝𝚒𝚘𝚗⚙️\n\n'
    msg+= '👤 𝙽𝚊𝚖𝚎: @' + str(username)+'\n'
    msg+= '👤 𝚄𝚜𝚎𝚛: ' + str(userdata['moodle_user'])+'\n'
    msg+= '🔑 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍: ' + str(userdata['moodle_password'])+'\n'
    msg+= '🌐 𝙲𝚕𝚘𝚞𝚍 𝚄𝚁𝙻: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '🆔 𝙲𝚕𝚘𝚞𝚍 𝙸𝙳: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= '☁️ 𝙲𝚕𝚘𝚞𝚍 𝚝𝚢𝚙𝚎: ' + str(userdata['cloudtype'])+'\n'
    msg+= '🔼 𝚄𝚙𝚕𝚘𝚊𝚍 𝚝𝚢𝚙𝚎: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '📁 𝙳𝚒𝚛𝚎𝚌𝚝𝚘𝚛𝚢: /' + str(userdata['dir'])+'\n'
    msg+= '🗜️ 𝚉𝚒𝚙𝚜 𝚜𝚒𝚣𝚎: ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = '𝙽𝚘'
    if isadmin:
        msgAdmin = '𝚈𝚎𝚜'
    msg+= '👮 𝙰𝚍𝚖𝚒𝚗𝚒𝚜𝚝𝚛𝚊𝚝𝚘𝚛: ' + msgAdmin + '\n'
    proxy = '𝙽𝚘'
    if userdata['proxy'] !='':
       proxy = '𝚈𝚎𝚜'
    tokenize = '𝙾𝚏𝚏'
    if userdata['tokenize']!=0:
       tokenize = '𝙾𝚗'
    msg+= '📡 𝙿𝚛𝚘𝚡𝚢 𝚜𝚎𝚝𝚝𝚎𝚍: ' + proxy + '\n'
    msg+= '🔒 𝙴𝚗𝚌𝚛𝚢𝚙𝚝 𝚕𝚒𝚗𝚔𝚜: ' + tokenize + '\n\n'
    msg+= '⚙️𝙲𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚎 𝚌𝚛𝚎𝚍𝚎𝚗𝚝𝚒𝚊𝚕𝚜⚙️\n 𝙴𝚡𝚊𝚖𝚙𝚕𝚎: /acc 𝚞𝚜𝚎𝚛,𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍'
    return msg
    
