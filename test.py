import webbrowser

def open_browser_tabs(links):
    print("Opening browser tabs...")
    for link in links:
        webbrowser.open_new_tab(link)
    print("Tabs opened successfully.")

if __name__ == "__main__":
    links = [
    "https://steamcommunity.com/sharedfiles/filedetails/?id=1794787369",
    "https://steamcommunity.com/sharedfiles/filedetails/?id=1820303287&searchtext=mirror+",
    "https://modsfire.com/Un12xb838hsJzc2",
    "https://steamcommunity.com/sharedfiles/filedetails/?id=648591060",
    "https://steamcommunity.com/sharedfiles/filedetails/?id=3071067969",
    "https://sharemods.com/mblati3mbin7/D.B_Creation_Traffic_Intensity_Pack.zip.html",
    "https://steamcommunity.com/sharedfiles/filedetails/?id=2827644973",
    "https://sharemods.com/nqzo9n2jbndl/Realistic_Brutal_Graphics_And_Weather_V9.5_By_Kass.rar.html",
    "https://sharemods.com/xo46rw8clnez/Tree_Improved__4k_2.0_ETS.scs.html",
    "https://sharemods.com/aecvvnvevpyx/Grass_3.0_ETS_4k.scs.html",
    "https://sharemods.com/k7b42adllqlf/better_raindrops_v1.9_ta_ets2.scs.html",
    "https://steamcommunity.com/sharedfiles/filedetails/?id=2980583543"
]

    open_browser_tabs(links)
