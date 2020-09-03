"""
!/usr/bin/env python3
__AUTHOR = "JIMOH IDRIS OLANSHILE"
__DATE = "Sept 2020 - till date."
"""
def doTrunc(event):
      def dele():
          data = "01"
          fO = open (f, "rb+")
          fO.read()
          count = fO.tell()
          data = data * int((count/2))
          fO.seek(0)
          fO.write (data.encode("utf-8"))
          fO.close()
      ans = mb.askquestion ("Confirmation", "Do you really want to truncate all of your hidden files?")
      if ans == "no":pass
      else:
          try:
              passes = 5
              num1 = 0
              num2 = 0
              cur.execute ("SELECT file FROM files WHERE user_login = " + "\"" + u_ + "\" ")
              for files in cur: #temp uh
                  files = files[0]
                  lFile = "\"" + files + "\""
                  lFile = lFile.replace ("\\", "/")
                  gd.system (anon + lFile + " -h -r -s -a")
                  F2d = files #unlike system, enc doesnt require the path to the quoted
                  newF2d = files.rpartition (".idr")[0]
                  dec (F2d, newF2d, password, bufferSize)
                  gd.system ("del " + "\"" + F2d.replace ("/", "\\") + "\"")
                  #gd.system ("del " + "\"" + newF2d.replace ("/", "\\") + "\"")
                  #lFile = lFile.replace ("\\", "\\\\")
                  f = newF2d.replace ("\\", "/")
                  num1 += 1
                  for i in range (0, int(passes)):
                      dele()
                      clr()
                  gd.rename (f, "zz028")
                  gd.unlink("zz028")
              cur.execute ("SELECT file FROM securenote WHERE user_login = " + "\"" + u_ + "\" ")
              for files in cur: #temp uh
                  files = files[0]
                  lFile = "\"" + files + "\""
                  lFile = lFile.replace ("/", "\\")
                  gd.system (anon + lFile + " -h -r -s -a")
                  F2d = files #unlike system, enc doesnt require the path to the quoted
                  newF2d = files.rpartition (".idr")[0]
                  dec (F2d, newF2d, password, bufferSize)
                  gd.system ("del " + "\"" + F2d.replace ("/", "\\") + "\"")
                  #gd.system ("del " + "\"" + newF2d.replace ("/", "\\") + "\"")
                  #lFile = lFile.replace ("\\", "\\\\")
                  f = newF2d
                  num2 += 1
                  for i in range (0, int(passes)):
                      dele()
                      clr()
                  gd.rename (f, "zz028")
                  gd.unlink("zz028")
              cur.execute ("truncate files")
              cur.execute ("truncate securenote")
              numTot = num1 + num2
              mb.showinfo ("Success", str (numTot) + " files just got truncated")
              conn.commit()
              clr()
          except OSError:
              logLab = Label (secNoteP, text = "  Error (0%)", bg = "#363277", fg = "WHITE")
              logLab.place (x = 0, y = 517)
