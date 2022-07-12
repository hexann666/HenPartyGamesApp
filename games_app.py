import streamlit as st
import games

st.image('data/header.jpg')
#st.title('Hen Party Games')

# setup pages for each use case
with st.expander('Never Have I ever'):
    st.markdown('1. Either designate someone to read each question or choose to take it in turns.')
    st.markdown('2. Take a drink if you have done what the question says e.g. ‘never have I ever been drunk’ if you have been drunk then take a drink!')
    if st.button('Challenge me!'):
        st.markdown(games.NeverHaveIEver())

with st.expander('Would You Rather'):
    if st.button('Surprise me!'):
        st.markdown(games.WouldYouRather())

with st.expander("Drunk Pictionary"):
    st.markdown('One hen must write down a word in a notepad that relates to a certain topic. \
        The hen who is deciding the word must state the topic it is to the hens so they have a \
        general idea on what the word will relate to.')
    st.markdown('The hen must then pass this secretive word onto a nominated drawer before the \
        timer begins. It is then the duty of the drawer to sketch the word as quickly as possible \
        leaving the group to guess what it is. Every 10 seconds, every guesser taking part must \
        sip their drink and keep going until they’ve guessed correctly.')
    st.markdown('The hen who is drawing cannot say anything or give any clues away, only express \
        what the word is through the form of art. ')
    st.markdown('If nobody has guessed after a minute, everyone must either down their drink or \
        go and buy a deadly shot from the bar.')
    category_list = ['None',
                'A Type of Food',
                'A TV Show',
                'A Film',
                'An Object',
                'An Action',
                'A Character',
                #'A Celebrity',
                'An Animal',
                'A Building',
                'A Nationality']
    cat = st.selectbox('Categories', category_list)
    st.markdown(games.DrunkPictionary(cat))




