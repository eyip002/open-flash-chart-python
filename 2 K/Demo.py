import	cherrypy
import	socket
import	math

from OpenFlashChart import Chart


class Demo:

	@cherrypy.expose
	def index(self):
		graphs = []
		
		# Line Charts
		graphs.append(flashHTML('100%', '400', '/line', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/bar1', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/bar2', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/bar3', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/hbar', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/stack', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/area', 'Getting there...', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/pie', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/scatter', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/radar', '/flashes/'))
		graphs.append(flashHTML('100%', '400', '/candle', '/flashes/'))

		graphs.append(self.source("html_snippet.html"))
	
		return self.source("OFC.htm") %({"chart": "<br/><br/><br/><br/>".join(graphs)})
		

	@cherrypy.expose
	def line(self):
		# Start with the data.  Each group of data to be plotted is called an
		# "element" in the json string.  The Chart class can be used to create
		# a container to store a group of data (even though you use it to create
		# the chart). 
		
		# First line data
		element1 = Chart()
		element1.type = "line"
		element1.values = [math.sin(float(x)/5) + 10 for x in range(0, 30)]
		element1.on_show.type = "pop-up"
		element1.on_show.cascade = 1
		element1.on_show.delay = 0.5
		
		# Second line data
		element2 = Chart()
		element2.type = "line"
		element2.values = [math.sin(float(x)/5) + 9 for x in range(0, 30)]
		element2.dot_style.type = "dot"
		element2.dot_style.colour = "#f00000"
		element2.width = 3
		element2.line_style.style = "dash"
		element2.line_style.on = 4
		element2.line_style.off = 8

		# Third line data
		element3 = Chart()
		element3.type = "line"
		element3.values = [math.sin(float(x)/5) + 8 for x in range(0, 30)]
		element3.dot_style =	{
									"type": "solid-dot",
									"dot-size": 4,
									"halo-size": 2,
									"colour": "#3D5C56"
								}
		element3.width = 6
		element3.colour = "#3D5C56"

		# Fourth line data
		element4 = Chart()
		element4.type = "line"
		element4.values = [math.sin(float(x)/5) + 7 for x in range(0, 30)]
		element4.dot_style =	{
									"type": "hollow-dot",
									"dot-size": 5,
									"halo-size": 2,
									"colour": "#3D5C56"
								}
		element4.width = 4
		element4.colour = "#f00000"

		# Fifth line data
		element5 = Chart()
		element5.type = "line"
		element5.values = [math.sin(float(x)/5) + 6 for x in range(0, 30)]
		element5.dot_style =	{
									"type": "star",
									"dot-size": 6,
									"halo-size": 2,
									"rotation": 180,
									"hollow": False,
								}
		element5.width = 2

		# Sixth line data
		element6 = Chart()
		element6.type = "line"
		element6.values = [math.sin(float(x)/5) + 5 for x in range(0, 30)]
		element6.dot_style =	{
									"type": "bow",
									"dot-size": 6,
									"halo-size": 2,
									"rotation": 70,
									"hollow": False,
								}
		element6.width = 2


		# Seventh line data (has one custom data value)
		element7_a = Chart()
		element7_a.type = "star"
		element7_a.value = 4
		element7_a.colour = "#D02020"
		element7_a.tip = "#val#<br>Your text here<br>Special"
		element7_a.on_click = "http://example.com"
		element7 = Chart()
		element7.type = "line"
		element7.values =  [element7_a] + [math.sin(float(x)/5) + 4 for x in range(0, 29)]
		element7.dot_style =	{
									"type": "dot",
									"dot-size": 6,
									"halo-size": 2,
									"on-click": "line_element7",
								}
		element7.width = 2


		# Eighth line data (scatter line)
		element8_a = Chart()
		element8_a.x = 1
		element8_a.y = 1
		element8_b = Chart()
		element8_b.x = 2
		element8_b.y = 3.5
		element8_c = Chart()
		element8_c =	[
							{"x": 2.0, "y": 1.3},
							{"x": 2.8, "y": 1.3},
							{"x": 5.1, "y": 3.5},
							{"x": 9.3, "y": 0.8},
							{"x": 16.4, "y": 3.4},
							{"x": 25.9, "y": 1.9},
						]
		element8 = Chart()
		element8.type = "scatter_line"
		element8.colour = "#6D8F47"
		element8.width = 3
		element8.values = [element8_a, element8_b] + element8_c
		element8.text = "No step"
		element8.font_size = 10
		element8.dot_style.type = "hollow-dot"
		element8.dot_style.dot_size = 3
		element8.dot_style.halo_size = 2



		# Now it's time to create the graphing area.  The method of adding attributes
		# is as easy as appending the attribute name to the end of your Chart instance
		# using dot notation.  Convert any dashes to underscores since Python doesn't
		# allow dashes in object names (dash is an operator).  

		# Create chart object
		chart = Chart()
		chart.title.text = "Lots of lines"
		chart.y_axis.min = 0
		chart.y_axis.max = 15
		chart.y_axis.steps = 5
		chart.tooltip.shadow = True
		chart.tooltip.stroke = 5
		chart.tooltip.colour = "#6e604f"
		chart.tooltip.background = "#bdb396"
		chart.tooltip.title = "{font-size: 14px; color: #CC2A43;}"
		chart.tooltip.body = "{font-size: 10px; font-weight: bold; color: #000000;}"

		# Add data to chart object
		chart.elements = [element1, element2, element3, element4, element5, element6, element7, element8]

		# Create chart json string
		return chart.create()

	@cherrypy.expose
	def bar1(self):
		# First bar data
		element1 = Chart()
		element1.type = "bar"
		element1.values = [9, 10]
		element1.on_show.type = "pop"
		element1.text = "First"
		
		# Second bar data
		element2 = Chart()
		element2.type = "bar_filled"
		element2.colour = "#e2d66a"
		element2.outline_colour = "#577261"
		element2.values = [7, 3]
		element2.on_show.type = "grow-up"
		
		# Third bar data
		element3_a = Chart()
		element3_a.top = 5
		element3_a.colour = "#ff0000"
		element3_a.tip = "Hello<br>#val#"
		element3 = Chart()
		element3.type = "bar_glass"
		element3.values = [10, element3_a]
		
		# Fourth bar data
		element4_a = Chart()
		element4_a.top = 8
		element4_a.colour = "#D54C78"
		element4 = Chart()
		element4.type = "bar_3d"
		element4.values = [15, element4_a]
		
		# Fifth bar data
		element5_a = Chart()
		element5_a.top = 11
		element5_a.colour = "#D54C78"
		element5 = Chart()
		element5.type = "bar_sketch"
		element5.values = [12, element5_a]
		element5.colour = "#81AC00"
		element5.outline_colour = "#567300"
		element5.offset = 20
		
		# Sixth bar data
		element6 = Chart()
		element6.type = "bar_cylinder"
		element6.values = [9, 10]

		# Create chart object
		chart = Chart()
		chart.title.text = "Lots of bars"
		chart.x_axis.threeD = 5
		chart.y_axis.min = 0
		chart.y_axis.max = 15
		chart.y_axis.steps = 5
		chart.bg_colour = "#ddffdd"

		# Add data to chart object
		chart.elements = [element1, element2, element3, element4, element5, element6]

		# Create chart json string
		return chart.create()

	@cherrypy.expose
	def bar2(self):
		# First bar data
		element1 = Chart()
		element1.type = "bar_round"
		element1.values = [9, 10]

		# Second bar data
		element2 = Chart()
		element2.type = "bar_round_glass"
		element2.values = [5, 12]

		# Third bar data
		element3 = Chart()
		element3.type = "bar_dome"
		element3.values = [12, 11]

		# Fourth bar data
		element4 = Chart()
		element4.type = "bar_cylinder_outline"
		element4.values = [2, 3]

		# Create chart object
		chart = Chart()
		chart.title.text = "Lots of bars"
		chart.x_axis.threeD = 5
		chart.y_axis.min = 0
		chart.y_axis.max = 15
		chart.y_axis.steps = 5
		chart.bg_colour = "#ddffdd"
		
		chart.menu.colour = "#e0e0ff"
		chart.menu.outline_colour = "#707070"
		chart.menu.values = [
								{"type": "camera-icon", "text": "Hello"},
								{"text": "Eugenuity"},
							]

		# Add data to chart object
		chart.elements = [element1, element2, element3, element4]

		# Create chart json string
		return chart.create()

	@cherrypy.expose
	def bar3(self):
		# First bar data
		values = [(6, 2), (7, 2), (10, 3), (13, 6), (17, 8), (20, 12), (22, 14), (21, 13), (19, 11), (14, 8), (10, 5), (7, 4)]
		element1 = Chart()
		element1.type = "bar_filled"
		element1.values = [{"top": t, "bottom": b} for (t, b) in values]

		# First line data
		element2 = Chart()
		element2.type = "line"
		element2.values = [5*math.sin(x) + 10 for x in range(0, 12)]
		element2.dot_style.type = "solid-dot"

		# Create chart object
		chart = Chart()
		chart.title.text = "Lots of bars"
		chart.y_axis.min = 0
		chart.y_axis.max = 30
		chart.y_axis.steps = 5
		chart.x_axis.labels.labels = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
		chart.bg_colour = "#ffffff"
		chart.tooltip.mouse = 2

		# Add data to chart object
		chart.elements = [element1, element2]

		# Create chart json string
		return chart.create()

	@cherrypy.expose
	def hbar(self):
		# First bar data
		values = [(0, 4), (4, 8)]
		element1 = Chart()
		element1.type = "hbar"
		element1.values = [{"left": l, "right": r} for (l, r) in values]
		element1.values += [{"left": 8, "right": 11, "tip": "#left# to #right#<br>Sept to Dec (#val# months)"}]
		element1.colour = "#86bbef"
		element1.tip = "Months: #val#"
		
		# First shape data
		shape1 = Chart()
		shape1.type = "shape"
		shape1.colour = "#fa6900"
		shape1.values = [{"x": x, "y": y} for (x, y) in [(4, 2.03), (4.65, 2.03), (4.65, 1.97), (4, 1.97)]]
		
		# Second shape data
		shape2 = Chart()
		shape2.type = "shape"
		shape2.colour = "#fa6900"
		shape2.values = [{"x": x, "y": y} for (x, y) in [(4.53, 1.97), (4.53, 1.6), (4.65, 1.6), (4.65, 1.97)]]
		
		# Third shape data
		shape3 = Chart()
		shape3.type = "shape"
		shape3.colour = "#fa6900"
		shape3.values = [{"x": x, "y": y} for (x, y) in [(4.3, 1.6), (4.59, 1.4), (4.87, 1.6)]]
		
		
		# Create chart object
		chart = Chart()
		chart.title.text = "Our New House Schedule"
		chart.y_axis.offset = 1
		chart.y_axis.labels = ["Make garden look sexy", "Paint house", "Move into house"]
		chart.x_axis.labels.labels = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
		chart.x_axis.offset = False

		# Add line data to chart object
		chart.elements = [element1, shape1, shape2, shape3]
		# First line data
		element1 = Chart()
		element1.type = "line"
		element1.values = [math.sin(float(x)/5) + 10 for x in range(0, 30)]
		element1.on_show.type = "pop-up"
		element1.on_show.cascade = 1
		element1.on_show.delay = 0.5
		
		# Create json string
		return chart.create()

	@cherrypy.expose
	def stack(self):
		# First bar stack data
		element1 = Chart()
		element1.type = "bar_stack"
		element1.values = [[2.5, 5, 2.5], [2.5, 5, 1.25, 1.25], [5, {"val": 5, "colour": "#ff0000"}], [2, 2, 2, 2, 2]]
		element1.colours = ["#C4D318", "#50284A", "#7D7B6A"]
		element1.keys = [
							{"colour": "#C4D318", "text": "Kiting", "font-size": 13},
							{"colour": "#50284A", "text": "Work", "font-size": 13},
							{"colour": "#7D7B6A", "text": "Drinking", "font-size": 13},
							{"colour": "#ff0000", "text": "XXX", "font-size": 13},
						]
		element1.tip = "X label [#x_label#], Value [#val#]<br>Total [#total#]"

		# Create chart object
		chart = Chart()
		chart.title.text = "Our New House Schedule"
		chart.title.style = "{font-size: 20px; color: #F24062; text-align: center;}"
		chart.y_axis.min = 0
		chart.y_axis.max = 14
		chart.y_axis.steps = 2
		chart.x_axis.labels.labels = ["Winter", "Spring", "Summer", "Autumn"]
		chart.tooltip.mouse = 2

		# Add data to chart object
		chart.elements = [element1]
		
		# Create chart json string
		return chart.create()

	@cherrypy.expose
	def area(self):
		# First area data
		element1 = Chart()
		element1.type = "area"
		element1.width = 2
		element1.dot_style = {"type": "dot", "colour": "#9C0E57", "dot-size": 7}
		element1.colour = "#C4B86A"
		element1.fill = "#C4B86A"
		element1.fill_alpha = 0.7
		element1.values = [math.sin(float(x)/10) for x in range(0, 60)]
		element1.on_show.type = "pop-up"
		element1.axis = "right"
		element1.text = "Sine wave"
		
		# Create chart object
		chart = Chart()
		chart.title.text = "Lots of area to cover"
		chart.title.style = "{font-size: 20px; color: #F24062; text-align: center;}"
		
		chart.y_axis.min = 35
		chart.y_axis.max = 55
		chart.y_axis.steps = 2
		chart.y_axis.labels.text = "$#val# million"
		chart.y_axis.labels.size = 16
		chart.y_axis.offset = 0
		chart.y_axis.stroke = 5
		chart.y_axis.colour = "#000000"
		chart.y_axis.tick_length = 10
		chart.y_axis.grid_colour = "#A2ACBA"
		
		chart.y_axis_right.min = -1.1
		chart.y_axis_right.max = 1.1
		chart.y_axis_right.steps = 2
		chart.y_axis_right.stroke = 3
		chart.y_axis_right.colour = "#3D5C56"
		chart.y_axis_right.tick_length = 12
		
		chart.x_axis.labels.steps = 4
		chart.x_axis.labels.rotate = 270
		chart.x_axis.labels.colour = "#00ff00"
		chart.x_axis.labels.size = 12
		chart.x_axis.steps = 2
		chart.x_axis.tick_height = 10
		chart.x_axis.stroke = 3
		chart.x_axis.colour = "#A2ACBA",
		chart.x_axis.grid_colour = "#D7E4A3"
		chart.x_axis.offset = False

		chart.x_legend.text = "Some numbers"
		chart.x_legend.style = "{font-size: 20px; color: #778877}"

		chart.y_legend.text = "Some text"
		chart.y_legend.style = "{font-size: 20px; color: #778877}"
		
		# Add data to chart object
		chart.elements = [element1]
		
		# Create chart json string
		return chart.create()

	@cherrypy.expose
	def pie(self):
		# First pie data
		element1 = Chart()
		element1.type = "pie"
		element1.alpha = 0.6
		element1.start_angle = 35
		element1.animate = [{"type": "fade"}, {"type": "bounce", "distance": 10}]
		element1.tip = "#val# of #total#<br>#percent# of 100%"
		element1.colours = ["#1C9E05", "#FF368D"]
		element1.gradient_fill = True
		element1.values = [2000, 3000, 4000, {"value": 6000.511, "label": "hello (6000.51)", "on-click": "http://example.com"}]
		element1.radius = 100
	
		# Create chart object
		chart = Chart()
		chart.title.text = "Hmmm pies"
		chart.num_decimals = 2
		chart.is_fixed_num_decimals_forced = True
		chart.is_decimal_separator_comma = False
		chart.is_thousand_separator_disabled = False
		
		# Add data to chart object
		chart.elements = [element1]
		
		# Create chart json string
		return chart.create()
	
	@cherrypy.expose
	def scatter(self):
		# First scatter data
		element1 = Chart()
		element1.type = "scatter"
		element1.colour = "#ffd600"
		element1.dot_style = {"type": "star", "colour": "#8b1d55", "dot-size": 10}
		element1.values = [{"type": "star", "x": 0, "y": 0}]
		
		# Second scatter data
		values = [(math.cos(float(i)/100), math.sin(float(i)/100)) for i in range(0, 628, 10)]
		element2 = Chart()
		element2.type = "scatter"
		element2.colour = "#d600ff"
		element2.dot_style = {"type": "anchor", "colour": "#D600FF", "dot-size": 4, "rotation": 45, "sides": 4}
		element2.values = [{"x": x, "y": y} for (x, y) in values]
		
		
		# Create chart object
		chart = Chart()
		chart.title.text = "Spark"
		chart.x_axis.min = -1.1
		chart.x_axis.max = 1.1
		chart.y_axis.min = -1.1
		chart.y_axis.max = 1.1
		chart.tooltip.mouse = 1
		
		# Add data to chart object
		chart.elements = [element1, element2]
		
		# Create chart json string
		return chart.create()


	@cherrypy.expose
	def radar(self):
		# First radar data
		element1 = Chart()
		element1.type = "area"
		element1.dot_style = {"type": "hollow-dot", "colour": "#45909f", "dot-size": 5}
		element1.colour = "#45909F"
		element1.fill = "#45909F"
		element1.fill_alpha = 0.4
		element1.loop = True
		element1.values = [3, 4, 5, 4, 3, 3, 2.5] + [{"value": 2, "tip": "Value at this spoke:<br>#val#"}]

		# Create chart object
		chart = Chart()
		chart.title.text = "Flight control"
		chart.radar_axis.max = 5
		chart.radar_axis.colour = "#efd1ef"
		chart.radar_axis.labels.labels = [str(i) for i in range(0, 6)]
		chart.radar_axis.labels.colour = "#9f819f"
		chart.tooltip.mouse = 1
		chart.bg_colour = "#dfffec"
		
		# Add data to chart object
		chart.elements = [element1]
		
		# Create chart json string
		return chart.create()

	@cherrypy.expose
	def candle(self):
		# First candle data
		data = []
		for x in range(0, 30):
			high = 4*math.sin(float(x)/2) + 14
			top = high - 4 - 2*math.sin(x/2)		# Actually the open price
			bottom = high - 4 - 2*math.cos(x/2)		# Actually the close price
			low = high - 8
			data.append({"high": high, "top": top, "bottom": bottom, "low": low})
		
		element1 = Chart()
		element1.type = "candle"
		element1.colour = "#9933cc"
		element1.values = data
		element1.tip = "#x_label#<br>High: #high#<br>Open: #open#<br>Close: #close#<br>Low: #low#"
		element1.alpha = 0.2
		
		# Create chart object
		chart = Chart()
		chart.title.text = "Predictable market movements"
		chart.y_axis.min = 0
		chart.y_axis.max = 20
		chart.y_axis.steps = 5

		# Add data to chart object
		chart.elements = [element1]
		
		# Create chart json string
		return chart.create()
		
		
		
	# Create a chart object for use
	# with the ajax function
	
	# Chart data
	ajaxElement = Chart()
	ajaxElement.values = [math.sin(float(x)/5) for x in range(0, 30)]
	ajaxElement.on_show.type = "pop-up"
	ajaxElement.on_show.cascade = 1
	ajaxElement.on_show.delay = 0.5
	ajaxElement.fill = "#333333"
	ajaxElement.fill_alpha = 0.7
	
	# Create ajax chart object
	ajaxChart = Chart()
	ajaxChart.title.text = "Different charts"
	ajaxChart.tooltip.mouse = 1
	ajaxChart.bg_colour = "#dfffec"
	ajaxChart.y_axis.min = -1.1
	ajaxChart.y_axis.max = 1.1
	ajaxChart.y_axis.steps = 2
	
	@cherrypy.expose
	def ajax(self, chartType):
		# Update chart type
		self.ajaxElement.type = chartType
		
		# Overwrite existing chart element data with new
		self.ajaxChart.elements = [self.ajaxElement]

		# Create chart json string
		return self.ajaxChart.create()





	def source(self, filename):
		"""Opens a file specified by the file/pathname in read-only"""
		file = open(filename, 'r')
		result = file.read()
		file.close()
		return result

	@cherrypy.expose
	def flashes(self, filename):
		cherrypy.response.headers['Content-Type'] = "application/x-shockwave-flash"
		cherrypy.response.headers['Expires'] = "Tue, 01 Dec 2009 12:00:00 GMT"
		cherrypy.response.headers['Cache-Control'] = "Public"
		return open(filename)


		

	
def flashHTML(width, height, url, loading_message = "Loading...", ofc_base_url="/flashes/", ofc_swf="OFC.swf" ):
	return (
		"""
		<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
				codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=9,0,115,0"
				width="%(width)s" height="%(height)s" id="chart" align="middle">
			<param name="allowScriptAccess" value="sameDomain"/>
			<param name="movie" value="%(ofc_base_url)s%(ofc_swf)s"/>
			<param name="FlashVars" value="data-file=%(url)s&loading=%(loading_message)s"/>
			<param name="quality" value="high"/>
			<param name="bgcolor" value="#FFFFFF"/>
			<embed src="%(ofc_base_url)s%(ofc_swf)s" FlashVars="data-file=%(url)s&loading=%(loading_message)s" quality="high" bgcolor="#FFFFFF"
				   width=%(width)s height=%(height)s name="chart" align="middle" allowScriptAccess="sameDomain"
				   type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer"/>
		</object>
		""") % locals()
	



cherrypy.server.socket_host = socket.gethostbyname(socket.gethostname())
cherrypy.quickstart(Demo(), config = 'serverconfig.conf')

