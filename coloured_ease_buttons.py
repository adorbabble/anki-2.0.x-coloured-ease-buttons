# -*- coding: utf-8 -*-
from aqt.reviewer import Reviewer

myBottomCSS = """
body {
background: -webkit-gradient(linear, left top, left bottom,
from(#fff), to(#ddd));
border-bottom: 0;
border-top: 1px solid #aaa;
margin: 0;
padding: 0px;
padding-left: 5px; padding-right: 5px;
}
button {
min-width: 60px; white-space: nowrap;
}
.hitem { margin-top: 2px; }
.stat { padding-top: 5px; }
.stat2 { padding-top: 3px; font-weight: normal; }
.stattxt { padding-left: 5px; padding-right: 5px; white-space: nowrap; }
.nobold { font-weight: normal; display: inline-block; padding-top: 4px; }
.spacer { height: 18px; }
.spacer2 { height: 16px; }
.btn-ease { padding: 0; border: none; border-radius: 3px }
.btn-ease:focus { outline: none; box-shadow: 0px 0px 15px 6px rgba(255, 190, 14, .7); }
.btn-i-ease { color: white; font-weight: bold; padding: 5px }
.btn-i-again { background: #d32f2f }
.btn-i-hard { background: #455a64 }
.btn-i-good { background: #4caf50 }
.btn-i-easy { background: #03a9f4 }
"""

def myAnswerButtonList(self):
    l = ((1, "<div class='btn-i-ease btn-i-again'>" + _("Again") + "</div>"),)
    cnt = self.mw.col.sched.answerButtons(self.card)
    if cnt == 2:
        return l + ((2, "<div class='btn-i-ease btn-i-good'>" + _("Good") + "</div>"),)
    elif cnt == 3:
        return l + ((2, "<div class='btn-i-ease btn-i-good'>" + _("Good") + "</div>"), (3, "<div class='btn-i-ease btn-i-easy'>" + _("Easy") + "</div>"))
    else:
        return l + ((2, "<div class='btn-i-ease btn-i-hard'>" + _("Hard") + "</div>"), (3, "<div class='btn-i-ease btn-i-good'>" + _("Good") + "</div>"), (4, "<div class='btn-i-ease btn-i-easy'>" + _("Easy") + "</div>"))

def myAnswerButtons(self):
    times = []
    default = self._defaultEase()
    def but(i, label):
        if i == default:
            extra = "id=defease"
        else:
            extra = ""
        due = self._buttonTime(i)
        return '''
<td align=center>%s<button %s title="%s" onclick='py.link("ease%d");' class="btn-ease">\
%s</button></td>''' % (due, extra, _("Shortcut key: %s") % i, i, label)
    buf = "<center><table cellpading=0 cellspacing=0><tr>"
    for ease, label in self._answerButtonList():
        buf += but(ease, label)
    buf += "</tr></table>"
    script = """
<script>$(function () { $("#defease").focus(); });</script>"""
    return buf + script

Reviewer._bottomCSS = myBottomCSS
Reviewer._answerButtonList = myAnswerButtonList
Reviewer._answerButtons = myAnswerButtons
