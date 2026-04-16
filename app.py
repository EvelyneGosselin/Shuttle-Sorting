#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Few original stops to not have an empty algorithm
stop_dictionnary = [{"stop_name": "Main Hall",      "crowd_count": 45},
    {"stop_name": "The ARC",     "crowd_count": 31},
    {"stop_name": "Theological hall",        "crowd_count": 58},
    {"stop_name": "University Avenue", "crowd_count": 72},
    {"stop_name": "Leonard hall",    "crowd_count": 19},
    {"stop_name": "Goodes",      "crowd_count": 63},
    {"stop_name": "Bioscience",  "crowd_count": 40},
    {"stop_name": "West Campus",  "crowd_count": 27},]


# In[2]:


#Gradio
import gradio as gr


# In[3]:


#Validate the added stops 

def validate_input(stop_list):
    for stop in stop_list:
        if stop["stop_name"] == " ":
            return False, "The input needs to be a word."
        
        if not stop["stop_name"]:
            return False, "The input is missing a name for the stop."
        
        if not stop["crowd_count"]:
            return False, "The input is missing a count of the crowd for the stop."
        
        try:
            count = int(stop["crowd_count"])
        except ValueError:
            return False, "The crowd_count is invalid"
        
    return True, None
            


# In[4]:


#Merge sort
steps = []
def merge (first_half,second_half):
    list_m = [] # Initiate the merge list
    i = 0
    j = 0
    while i < len(first_half) and j < len(second_half):
        steps.append(f"Comparing {first_half[i]['stop_name']} ({first_half[i]['crowd_count']}) vs {second_half[j]['stop_name']} ({second_half[j]['crowd_count']})")
        if first_half[i]["crowd_count"] >= second_half[j]["crowd_count"]:
            list_m.append(first_half[i])
            steps.append(f"→ {first_half[i]['stop_name']} placed first")
            i +=1
        else:
            list_m.append(second_half[j])
            steps.append(f"→ {second_half[j]['stop_name']} placed first")
            j+=1
    while i < len(first_half):
        list_m.append(first_half[i])
        i += 1
    while j < len(second_half):
        list_m.append(second_half[j])
        j += 1
    return list_m

def sort(a):
    n = len(a)
    if n<2:
        return(a)
    else:
        first_half = a[:n//2]
        second_half = a[n//2:]
        return merge(sort(first_half), sort(second_half))
    
    
        
        


# In[5]:


# To add a stop to the list

def add_stop(stop_name, crowd_count_str):
    valid, error = validate_input([{"stop_name": stop_name, "crowd_count": crowd_count_str}])
    if not valid:
        return render_list(stop_dictionnary), error
    
    stop_dictionnary.append({"stop_name": stop_name.strip(), "crowd_count": int(crowd_count_str)})
    return render_list(stop_dictionnary), "Stop added."


# In[6]:


#Here is the actual code that runs using the functions we coded 

#Step 1: Validation of input
valid_bool, error_message = validate_input(stop_dictionnary)

if not valid_bool:
    print(error_message)
else:
    print("Valid input")

#Step 2: Sort
#sorted_list = sort(stop_dictionnary)

#Step 3: Displaying (for now just terminal)
#print("Order of stops that deserve extra shuttle")
#for rank in range(1, len(sorted_list)+1):
    #stop = sorted_list[rank-1]
    #if rank == 1:
        #indication_shuttle = "<-- send shuttle here"
    #else:
       # indication_shuttle = ""
   # print(f"{rank}. {stop['stop_name']:<20} crowd: {stop['crowd_count']} {indication_shuttle}")

def render_list(stop_list):
    output = ""
    for i in range(len(stop_list)):
        stop = stop_list[i]
        output += f"{i+1}. {stop['stop_name']:<20} crowd: {stop['crowd_count']}\n"
    return output

def sort_and_display():
    if len(stop_dictionnary) < 2:
        return "Add at least 2 stops before sorting.", ""
    sorted_list = sort(stop_dictionnary.copy())
    result = ""
    for rank in range(1, len(sorted_list) + 1):
        stop = sorted_list[rank - 1]
        indication = "<-- send shuttle here!" if rank == 1 else ""
        result += f"{rank}. {stop['stop_name']:<20} crowd: {stop['crowd_count']} {indication}\n"
    return result, ""

with gr.Blocks(title="Shuttle Stop Crowd Ranking") as demo:

    gr.Markdown("# Shuttle Stop Crowd Ranking")
    gr.Markdown("Add stops and sort by crowd count to decide where to send the shuttle.")

    # Input
    with gr.Row():
        name_input  = gr.Textbox(label="Stop Name",   placeholder="")
        count_input = gr.Textbox(label="Crowd Count", placeholder="")
    
    with gr.Row():
        add_btn  = gr.Button("Add Stop",      variant="primary")
        sort_btn = gr.Button("Sort Stops", variant="primary")

    status_msg      = gr.Textbox(label="Status",          interactive=False)
    current_display = gr.Textbox(label="Current Stops",   interactive=False, lines=10, value=render_list(stop_dictionnary))
    result_display  = gr.Textbox(label="Sorted Ranking",  interactive=False, lines=10)

    add_btn.click(fn=add_stop,        inputs=[name_input, count_input], outputs=[current_display, status_msg])
    sort_btn.click(fn=sort_and_display, outputs=[result_display, status_msg])

demo.launch()


# In[ ]:





# In[ ]:




