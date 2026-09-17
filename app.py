from flask import Flask, request, render_template_string

app = Flask(__name__)

# =====================================================
# COLLEGE RESOURCES
# =====================================================

resources = [
    {"name": "Lab 1", "type": "Lab"},
    {"name": "Lab 2", "type": "Lab"},
    {"name": "Lab 3", "type": "Lab"},
    {"name": "Seminar Hall 1", "type": "Hall"},
    {"name": "Seminar Hall 2", "type": "Hall"},
    {"name": "Auditorium", "type": "Auditorium"}
]

# Store events
events = []


# =====================================================
# HTML + CSS
# =====================================================

HTML = """

<!DOCTYPE html>

<html>

<head>

<title>AI College Resource Resolver</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #eef2f7;
    color: #222;
}

/* HEADER */

header {
    background: linear-gradient(135deg, #182848, #4b6cb7);
    color: white;
    text-align: center;
    padding: 30px 15px;
}

header h1 {
    margin: 0 0 10px;
}

header p {
    margin: 0;
}

/* CONTAINER */

.container {
    width: 90%;
    max-width: 1200px;
    margin: 25px auto;
}

/* CARD */

.card {
    background: white;
    padding: 25px;
    margin-bottom: 20px;
    border-radius: 15px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
}

.card h2 {
    color: #182848;
    margin-top: 0;
}

/* INPUTS */

input,
select {
    padding: 12px;
    margin: 5px;
    border: 1px solid #ccc;
    border-radius: 7px;
    font-size: 14px;
}

input:focus,
select:focus {
    border-color: #4b6cb7;
    outline: none;
}

/* BUTTON */

button {
    padding: 12px 20px;
    background: #182848;
    color: white;
    border: none;
    border-radius: 7px;
    cursor: pointer;
    font-weight: bold;
}

button:hover {
    background: #4b6cb7;
}

/* RESOURCE */

.resource {
    display: inline-block;
    background: #e5ebff;
    color: #182848;
    padding: 10px 15px;
    margin: 5px;
    border-radius: 20px;
    font-weight: bold;
}

/* TABLE */

.table-container {
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th {
    background: #182848;
    color: white;
    padding: 13px;
}

td {
    padding: 12px;
    text-align: center;
    border-bottom: 1px solid #ddd;
}

tr:hover {
    background: #f5f7fb;
}

/* STATISTICS */

.stats {
    display: flex;
    gap: 15px;
    flex-wrap: wrap;
}

.stat {
    flex: 1;
    min-width: 180px;
    background: #f5f7fb;
    padding: 20px;
    text-align: center;
    border-radius: 12px;
}

.stat h1 {
    margin: 0;
    color: #182848;
    font-size: 35px;
}

/* SUCCESS */

.success {
    color: green;
    font-weight: bold;
}

/* CONFLICT */

.conflict {
    background: #fff0f0;
    border-left: 5px solid red;
    padding: 15px;
    margin: 10px 0;
    border-radius: 8px;
}

.warning {
    color: red;
    font-weight: bold;
}

/* AI BUTTON */

.ai-button {
    width: 100%;
    font-size: 17px;
    padding: 16px;
    background: linear-gradient(135deg, #182848, #4b6cb7);
}

/* EMPTY */

.empty {
    text-align: center;
    color: #777;
    padding: 20px;
}

/* FOOTER */

footer {
    background: #182848;
    color: white;
    text-align: center;
    padding: 25px;
    margin-top: 40px;
}

/* MOBILE */

@media(max-width: 700px) {

    input,
    select {
        width: 100%;
        margin: 5px 0;
    }

    .stats {
        flex-direction: column;
    }

}

</style>

</head>


<body>


<!-- =================================================
     HEADER
================================================== -->

<header>

<h1>🤖 AI College Resource Conflict Resolver</h1>

<p>
"When everyone wants the same resource, AI decides who gets what."
</p>

</header>


<div class="container">


<!-- =================================================
     RESOURCES
================================================== -->

<div class="card">

<h2>🏫 Available College Resources</h2>

{% for r in resources %}

<span class="resource">

{{ r.name }} - {{ r.type }}

</span>

{% endfor %}

</div>


<!-- =================================================
     ADD EVENT
================================================== -->

<div class="card">

<h2>📅 Add Event / Group Requirement</h2>

<form method="POST" action="/add">

<input
type="text"
name="group"
placeholder="Group e.g. AIML-A"
required
>

<input
type="text"
name="event"
placeholder="Event e.g. AI Practical"
required
>

<input
type="date"
name="date"
required
>

<input
type="text"
name="time"
placeholder="Time e.g. 10-12"
required
>

<br>

<select name="type">

<option value="Lab">
💻 Computer Lab
</option>

<option value="Hall">
🏛 Seminar Hall
</option>

<option value="Auditorium">
🎤 Auditorium
</option>

</select>


<select name="priority">

<option value="High">
🔴 High Priority
</option>

<option value="Medium">
🟡 Medium Priority
</option>

<option value="Low">
🟢 Low Priority
</option>

</select>


<select name="preferred">

<option value="">
No Preferred Resource
</option>

{% for r in resources %}

<option value="{{ r.name }}">

{{ r.name }}

</option>

{% endfor %}

</select>

<br><br>

<button type="submit">

➕ Add Event

</button>

</form>

</div>


<!-- =================================================
     EVENTS
================================================== -->

<div class="card">

<h2>👥 Requested Events</h2>

{% if events %}

<div class="table-container">

<table>

<tr>

<th>Group</th>
<th>Event</th>
<th>Date</th>
<th>Time</th>
<th>Type</th>
<th>Priority</th>

</tr>


{% for e in events %}

<tr>

<td>{{ e.group }}</td>

<td>{{ e.event }}</td>

<td>{{ e.date }}</td>

<td>{{ e.time }}</td>

<td>{{ e.type }}</td>

<td>{{ e.priority }}</td>

</tr>

{% endfor %}

</table>

</div>

{% else %}

<p class="empty">

No events added yet.

</p>

{% endif %}

</div>


<!-- =================================================
     AI BUTTON
================================================== -->

<div class="card">

<form method="POST" action="/generate">

<button class="ai-button">

🤖 GENERATE AI CONFLICT-FREE SCHEDULE

</button>

</form>

</div>


<!-- =================================================
     RESULT
================================================== -->

{% if result %}


<!-- STATISTICS -->

<div class="card">

<h2>📊 AI Results</h2>

<div class="stats">


<div class="stat">

<h1>
{{ result.total }}
</h1>

<p>Total Events</p>

</div>


<div class="stat">

<h1>
{{ result.allocated }}
</h1>

<p>Successfully Allocated</p>

</div>


<div class="stat">

<h1>
{{ result.conflicts }}
</h1>

<p>Conflicts</p>

</div>


<div class="stat">

<h1>
{{ result.success }}%
</h1>

<p>Success Rate</p>

</div>


</div>

</div>


<!-- =================================================
     GENERATED SCHEDULE
================================================== -->

<div class="card">

<h2>✅ AI Generated Schedule</h2>

{% if result.allocations %}

<div class="table-container">

<table>

<tr>

<th>Group</th>
<th>Event</th>
<th>Resource</th>
<th>Date</th>
<th>Time</th>
<th>Priority</th>
<th>Status</th>

</tr>


{% for a in result.allocations %}

<tr>

<td>{{ a.group }}</td>

<td>{{ a.event }}</td>

<td>🏫 {{ a.resource }}</td>

<td>{{ a.date }}</td>

<td>{{ a.time }}</td>

<td>{{ a.priority }}</td>

<td class="success">

✓ Allocated

</td>

</tr>

{% endfor %}

</table>

</div>

{% else %}

<p class="empty">
No events could be allocated.
</p>

{% endif %}

</div>


<!-- =================================================
     CONFLICTS
================================================== -->

<div class="card">

<h2>⚠️ Conflicts Detected</h2>


{% if result.conflict_list %}


{% for c in result.conflict_list %}

<div class="conflict">

<p class="warning">

❌ {{ c.group }} - {{ c.event }}

</p>

<p>
🕐 Time: {{ c.time }}
</p>

<p>
⚠️ Reason: {{ c.reason }}
</p>

</div>

{% endfor %}


{% else %}

<p class="success">

🎉 Perfect!

No conflicts found.

All events were successfully allocated.

</p>

{% endif %}


</div>


{% endif %}


</div>


<!-- =================================================
     FOOTER
================================================== -->

<footer>

<p>
🤖 AI College Resource Conflict Resolver
</p>

<p>
State Space Search • Heuristic Search • Constraint Satisfaction
</p>

</footer>


</body>

</html>

"""


# =====================================================
# TIME CONFLICT FUNCTION
# =====================================================

def time_overlap(time1, time2):

    try:

        start1, end1 = map(
            int,
            time1.split("-")
        )

        start2, end2 = map(
            int,
            time2.split("-")
        )

        return (
            start1 < end2
            and
            start2 < end1
        )

    except:

        return True


# =====================================================
# PRIORITY FUNCTION
# =====================================================

def priority_value(priority):

    if priority == "High":
        return 3

    elif priority == "Medium":
        return 2

    else:
        return 1


# =====================================================
# AI SCHEDULER
# =====================================================

def generate_schedule():

    allocations = []

    conflicts = []


    # -----------------------------------------------
    # AI STEP 1
    # HIGH PRIORITY EVENTS FIRST
    # -----------------------------------------------

    sorted_events = sorted(
        events,
        key=lambda x: priority_value(
            x["priority"]
        ),
        reverse=True
    )


    # -----------------------------------------------
    # PROCESS EACH EVENT
    # -----------------------------------------------

    for event in sorted_events:

        possible_resources = []


        # -------------------------------------------
        # SEARCH ALL RESOURCES
        # -------------------------------------------

        for resource in resources:

            # Resource type must match
            if resource["type"] != event["type"]:
                continue


            available = True


            # ---------------------------------------
            # CHECK EXISTING ALLOCATIONS
            # ---------------------------------------

            for allocated in allocations:

                if allocated["resource"] == resource["name"]:

                    if allocated["date"] == event["date"]:

                        if time_overlap(
                            allocated["time"],
                            event["time"]
                        ):

                            available = False


            # ---------------------------------------
            # CALCULATE HEURISTIC SCORE
            # ---------------------------------------

            if available:

                score = 10


                # Preferred resource
                if (
                    event["preferred"]
                    and
                    event["preferred"]
                    == resource["name"]
                ):

                    score += 100


                # Priority
                if event["priority"] == "High":

                    score += 30

                elif event["priority"] == "Medium":

                    score += 20

                else:

                    score += 10


                possible_resources.append(
                    (score, resource)
                )


        # -------------------------------------------
        # SELECT BEST RESOURCE
        # -------------------------------------------

        if possible_resources:

            possible_resources.sort(
                key=lambda x: x[0],
                reverse=True
            )


            best_resource = \
                possible_resources[0][1]


            allocations.append({

                "group":
                    event["group"],

                "event":
                    event["event"],

                "resource":
                    best_resource["name"],

                "date":
                    event["date"],

                "time":
                    event["time"],

                "priority":
                    event["priority"]

            })


        # -------------------------------------------
        # NO RESOURCE AVAILABLE
        # -------------------------------------------

        else:

            conflicts.append({

                "group":
                    event["group"],

                "event":
                    event["event"],

                "time":
                    event["time"],

                "reason":
                    "All suitable resources are occupied."

            })


    # =================================================
    # STATISTICS
    # =================================================

    total = len(events)

    allocated = len(allocations)

    conflict_count = len(conflicts)


    if total > 0:

        success = round(
            allocated / total * 100
        )

    else:

        success = 0


    return {

        "total":
            total,

        "allocated":
            allocated,

        "conflicts":
            conflict_count,

        "success":
            success,

        "allocations":
            allocations,

        "conflict_list":
            conflicts

    }


# =====================================================
# HOME PAGE
# =====================================================

@app.route("/")
def home():

    return render_template_string(

        HTML,

        resources=resources,

        events=events,

        result=None

    )


# =====================================================
# ADD EVENT
# =====================================================

@app.route("/add", methods=["POST"])
def add_event():

    new_event = {

        "group":
            request.form.get("group"),

        "event":
            request.form.get("event"),

        "date":
            request.form.get("date"),

        "time":
            request.form.get("time"),

        "type":
            request.form.get("type"),

        "priority":
            request.form.get("priority"),

        "preferred":
            request.form.get("preferred")

    }


    # Validate time
    try:

        start, end = map(
            int,
            new_event["time"].split("-")
        )

        if start >= end or start < 0 or end > 24:

            raise ValueError

    except:

        return """

        <h2>❌ Invalid Time</h2>

        <p>
        Please enter time like:
        <b>10-12</b>
        </p>

        <a href="/">
        ← Go Back
        </a>

        """


    events.append(new_event)


    return render_template_string(

        HTML,

        resources=resources,

        events=events,

        result=None

    )


# =====================================================
# GENERATE SCHEDULE
# =====================================================

@app.route("/generate", methods=["POST"])
def generate():

    result = generate_schedule()


    return render_template_string(

        HTML,

        resources=resources,

        events=events,

        result=result

    )


# =====================================================
# CLEAR ALL EVENTS
# =====================================================

@app.route("/clear", methods=["POST"])
def clear():

    events.clear()

    return render_template_string(

        HTML,

        resources=resources,

        events=events,

        result=None

    )


# =====================================================
# START APPLICATION
# =====================================================

if __name__ == "__main__":

    print("")
    print("==============================================")
    print(" 🤖 AI COLLEGE RESOURCE CONFLICT RESOLVER")
    print("==============================================")
    print("")
    print("Server started successfully!")
    print("")
    print("Open this in your browser:")
    print("http://127.0.0.1:5000")
    print("")
    print("==============================================")


    app.run(
        debug=False,
        use_reloader=False
    )