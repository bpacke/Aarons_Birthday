from datetime import date
import webbrowser as wb
class Friend:
	def __init__(self, name, dob, vid):
		self.name = name
		self.dob = dob
		self.vid = 'https://www.youtube.com/embed/%s?autoplay=1' % vid


friends = [Friend('Aaron', date(1993,03,17), 'jBm_6SKAML8'), Friend('Ben', date(1994,04,16), 'RHw50kjFuoA')]

t = date.today()

for f in friends:
	if t.day == f.dob.day and t.month == f.dob.month:
		print 'Happy Birthday, %s!' % f.name
		wb.get().open(f.vid)