import os
from functools import cache
import streamlit as st

st.set_page_config(
    layout="wide", initial_sidebar_state="collapsed", page_title="TTS Listening Tests."
)


def load_experiments():
    experiments = []
    for experiment in os.listdir("audio"):
        experiments.append(os.path.basename(experiment))
    return experiments


@cache
def load_experiment_data(experiment_name):
    experiment_data = {}
    n_rows, n_cols = [], []
    for data in os.listdir("audio/" + experiment_name):
        filename = os.path.basename(data)
        column_name = filename.split("_")[0]
        row_name = filename.split("_")[1]
        if row_name not in experiment_data:
            experiment_data[row_name] = {}
        experiment_data[row_name][
            column_name
        ] = "F:\Workspace\Python\AI4Bharat\Automatic Streamlit App/audio/new_experiment/train_hindifullmale_00384.wav"
        n_rows.append(row_name)
        n_cols.append(column_name)

    n_rows, n_cols = sorted(set(n_rows)), sorted(set(n_cols))

    return experiment_data, n_rows, n_cols


def load_page(page_name):
    st.session_state["page_name"] = f"listen_{page_name}"
    # st.button("Take Listening Test", on_click=test, args=(page_name,))
    if st.session_state["page_name"].startswith("listen_"):
        st.title(page_name)
        data, n_rows, n_cols = load_experiment_data(page_name)
        headers = ["ID"] + n_cols
        cols = st.columns(len(n_cols) + 1)
        for i in range(len(headers)):
            # if i == 0:
            #     cols[i].markdown(f"**ID**")
            cols[i].markdown(f"**{headers[i]}**")
        for row in n_rows:
            cols = st.columns(len(n_cols) + 1)
            cols[0].markdown(f"**{row}**")
            for i, col in enumerate(n_cols, start=1):
                if col in data[row]:
                    cols[i].audio(data[row][col])
                else:
                    cols[i].markdown(f" ")


def landing():
    st.title("AI4Bharat Speech Synthesis Team")
    st.header("About Us")
    st.write(
        "We are the AI4Bharat Speech Synthesis team, dedicated to advancing speech synthesis research and development."
    )

    # Our Projects section
    st.header("Our Projects")
    st.markdown(
        "- **Project 1:** Text-to-Speech (TTS) Research\n"
        "- **Project 2:** Voice Cloning\n"
        "- **Project 3:** Multilingual TTS\n"
        "- **Project 4:** Expressive Speech Synthesis\n"
        "- **Project 5:** Natural Speech\n"
    )

    # Team Members section
    st.header("Team Members")
    st.markdown(
        "- Praveen S V: TTS Research Lead\n"
        "- Ashwin Sankar: Expressive Speech Synthesis Lead\n"
        "- Srija Anand: Data Collection Lead\n"
        "- Richard: Full-Stack Developer\n"
    )

    # Showcase multimedia elements
    st.header("Media Showcase")
    # st.image(
    #     "https://avatars.githubusercontent.com/u/69502895?s=280&v=4",
    #     use_column_width=True,
    #     caption="AI4Bharat Team",
    # )

    # Contact Us section
    st.header("Contact Us")
    st.write(
        "If you have any questions or would like to collaborate with us, feel free to reach out:"
    )
    st.markdown("- Email: speech@ai4bharat.org")
    st.markdown("- Twitter: @AI4Bharat")

    # Footer
    st.write("© 2023 AI4Bharat Speech Synthesis Team")


def main():
    if "page_name" not in st.session_state:
        st.session_state["page_name"] = "Home"
        landing()

    experiments = load_experiments()
    st.sidebar.button("Home", on_click=landing)
    for experiment in experiments:
        st.sidebar.button(experiment, on_click=load_page, args=(experiment,))


if __name__ == "__main__":
    load_experiment_data.cache_clear()
    main()
