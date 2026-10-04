import streamlit as st
import time

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MicroDegree | Learning Platform",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------- GLOBAL -------------------- */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(99,102,241,0.08), transparent 25%),
            radial-gradient(circle at 90% 20%, rgba(14,165,233,0.08), transparent 25%),
            #f8fafc;
        color: #0f172a;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    /* -------------------- TOP BAR -------------------- */

    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 0 25px 0;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 45px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 11px;
        font-size: 22px;
        font-weight: 800;
        color: #0f172a;
    }

    .brand-mark {
        width: 40px;
        height: 40px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 20px;
        font-weight: 800;
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        box-shadow: 0 8px 20px rgba(79,70,229,0.25);
    }

    .brand-accent {
        color: #4f46e5;
    }

    .nav-pill {
        background: #eef2ff;
        color: #4f46e5;
        border: 1px solid #c7d2fe;
        padding: 8px 15px;
        border-radius: 30px;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.7px;
    }

    /* -------------------- HERO -------------------- */

    .hero {
        text-align: center;
        padding: 25px 0 35px 0;
    }

    .hero-badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 30px;
        background: #eef2ff;
        border: 1px solid #c7d2fe;
        color: #4338ca;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 18px;
    }

    .hero h1 {
        font-size: 46px;
        line-height: 1.12;
        letter-spacing: -1.5px;
        margin: 0;
        font-weight: 800;
        color: #0f172a;
    }

    .hero h1 span {
        color: #4f46e5;
    }

    .hero p {
        max-width: 680px;
        margin: 18px auto 0 auto;
        color: #64748b;
        font-size: 17px;
        line-height: 1.7;
    }

    /* -------------------- REGISTRATION CARD -------------------- */

    .registration-card {
        background: rgba(255,255,255,0.92);
        border: 1px solid #e2e8f0;
        border-radius: 24px;
        padding: 34px;
        box-shadow:
            0 20px 50px rgba(15,23,42,0.07),
            0 3px 10px rgba(15,23,42,0.03);
        margin-top: 10px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 6px;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 25px;
    }

    /* -------------------- INPUTS -------------------- */

    div[data-baseweb="input"] {
        border-radius: 12px;
    }

    div[data-baseweb="select"] {
        border-radius: 12px;
    }

    .stTextInput label,
    .stSelectbox label {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }

    .stTextInput input {
        border-radius: 12px !important;
        border: 1px solid #cbd5e1 !important;
        padding: 12px !important;
    }

    .stTextInput input:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99,102,241,0.12) !important;
    }

    /* -------------------- BUTTON -------------------- */

    .stButton > button {
        border: none;
        border-radius: 12px;
        min-height: 48px;
        font-weight: 700;
        font-size: 14px;
        color: white;
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        box-shadow: 0 8px 20px rgba(79,70,229,0.22);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(79,70,229,0.28);
    }

    /* -------------------- UNLOCK SECTION -------------------- */

    .unlock {
        text-align: center;
        padding: 35px 20px 25px 20px;
    }

    .unlock-icon {
        width: 74px;
        height: 74px;
        margin: 0 auto 18px auto;
        border-radius: 22px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 35px;
        background: linear-gradient(135deg, #eef2ff, #ede9fe);
        border: 1px solid #c7d2fe;
    }

    .unlock h1 {
        font-size: 38px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
    }

    .unlock p {
        color: #64748b;
        font-size: 16px;
    }

    .unlock-highlight {
        display: inline-block;
        margin-top: 15px;
        padding: 10px 18px;
        border-radius: 30px;
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        color: #047857;
        font-size: 13px;
        font-weight: 700;
    }

    /* -------------------- SECTION HEADERS -------------------- */

    .section-header {
        margin: 35px 0 18px 0;
    }

    .section-header h2 {
        font-size: 24px;
        margin: 0;
        color: #0f172a;
        font-weight: 800;
    }

    .section-header p {
        color: #64748b;
        margin-top: 5px;
        font-size: 14px;
    }

    /* -------------------- PROJECT CARDS -------------------- */

    .project-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 24px;
        height: 220px;
        box-shadow: 0 10px 25px rgba(15,23,42,0.05);
        transition: all 0.25s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 35px rgba(15,23,42,0.10);
        border-color: #c7d2fe;
    }

    .project-icon {
        width: 45px;
        height: 45px;
        border-radius: 13px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        background: #eef2ff;
        margin-bottom: 15px;
    }

    .project-level {
        color: #6366f1;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 0.8px;
        margin-bottom: 6px;
    }

    .project-card h3 {
        margin: 0 0 8px 0;
        color: #0f172a;
        font-size: 18px;
        font-weight: 800;
    }

    .project-card p {
        margin: 0;
        color: #64748b;
        font-size: 13px;
        line-height: 1.6;
    }

    /* -------------------- VIDEO CARDS -------------------- */

    .video-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 16px;
        box-shadow: 0 8px 22px rgba(15,23,42,0.05);
    }

    .video-title {
        font-size: 15px;
        font-weight: 800;
        color: #0f172a;
        margin: 12px 0 5px 0;
    }

    .video-description {
        font-size: 12px;
        color: #64748b;
        line-height: 1.5;
    }

    /* -------------------- CTA -------------------- */

    .cta {
        margin-top: 45px;
        padding: 38px;
        border-radius: 24px;
        background: linear-gradient(135deg, #111827, #312e81);
        color: white;
        text-align: center;
        box-shadow: 0 20px 45px rgba(15,23,42,0.18);
    }

    .cta h2 {
        font-size: 28px;
        margin: 0 0 8px 0;
        font-weight: 800;
    }

    .cta p {
        color: #cbd5e1;
        font-size: 14px;
        margin-bottom: 20px;
    }

    .cta a {
        display: inline-block;
        padding: 12px 22px;
        border-radius: 12px;
        background: white;
        color: #312e81;
        text-decoration: none;
        font-weight: 800;
        font-size: 13px;
        transition: 0.2s;
    }

    .cta a:hover {
        transform: translateY(-2px);
    }

    /* -------------------- STATS -------------------- */

    .stat-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(15,23,42,0.04);
    }

    .stat-number {
        font-size: 25px;
        font-weight: 800;
        color: #4f46e5;
    }

    .stat-label {
        margin-top: 5px;
        font-size: 12px;
        color: #64748b;
        font-weight: 600;
    }

    /* -------------------- FOOTER -------------------- */

    .footer {
        text-align: center;
        margin-top: 55px;
        padding-top: 25px;
        border-top: 1px solid #e2e8f0;
        color: #94a3b8;
        font-size: 12px;
    }

    /* -------------------- MOBILE -------------------- */

    @media (max-width: 768px) {

        .hero h1 {
            font-size: 34px;
        }

        .unlock h1 {
            font-size: 30px;
        }

        .registration-card {
            padding: 22px;
        }

        .topbar {
            margin-bottom: 25px;
        }

        .nav-pill {
            display: none;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SESSION STATE
# ============================================================

if "registered" not in st.session_state:
    st.session_state.registered = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "track" not in st.session_state:
    st.session_state.track = "Cloud Computing"


# ============================================================
# TOP BAR
# ============================================================

st.markdown(
    """
    <div class="topbar">
        <div class="brand">
            <div class="brand-mark">M</div>
            <div>
                Micro<span class="brand-accent">Degree</span>
            </div>
        </div>

        <div class="nav-pill">
            LEARNING PLATFORM
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# REGISTRATION PAGE
# ============================================================

if not st.session_state.registered:

    st.markdown(
        """
        <div class="hero">

            <div class="hero-badge">
                🚀 START YOUR LEARNING JOURNEY
            </div>

            <h1>
                Turn your potential into
                <span>real-world skills.</span>
            </h1>

            <p>
                Create your MicroDegree profile and unlock
                practical projects, curated learning resources,
                and cloud career content.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="registration-card">

            <div class="section-title">
                Create your learning profile
            </div>

            <div class="section-subtitle">
                Tell us a little about yourself so we can personalize your learning journey.
            </div>

        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # FORM
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "Email Address",
            placeholder="you@example.com"
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="+91 XXXXX XXXXX"
        )

    with col2:

        current_status = st.selectbox(
            "Current Status",
            [
                "Student",
                "Working Professional",
                "Fresher",
                "Career Switcher",
                "Other"
            ]
        )

        experience = st.selectbox(
            "Experience Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

        learning_track = st.selectbox(
            "Learning Track",
            [
                "Cloud Computing",
                "Python Development",
                "Data Engineering",
                "DevOps",
                "AI & Machine Learning"
            ]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    agreement = st.checkbox(
        "I agree to receive learning resources and updates from MicroDegree."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    submit = st.button(
        "🚀 Create Profile & Unlock Projects",
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # --------------------------------------------------------
    # FORM VALIDATION
    # --------------------------------------------------------

    if submit:

        errors = []

        if not full_name.strip():
            errors.append("Please enter your full name.")

        if not email.strip():
            errors.append("Please enter your email address.")

        elif "@" not in email or "." not in email.split("@")[-1]:
            errors.append("Please enter a valid email address.")

        if not agreement:
            errors.append("Please accept the communication agreement.")

        if errors:

            for error in errors:
                st.error(error)

        else:

            st.session_state.user_name = full_name.strip()
            st.session_state.registered = True
            st.session_state.track = learning_track

            st.balloons()

            time.sleep(1)

            st.rerun()


# ============================================================
# SUCCESS / UNLOCKED PAGE
# ============================================================

else:

    st.markdown(
        f"""
        <div class="unlock">

            <div class="unlock-icon">
                🎉
            </div>

            <h1>
                Welcome, {st.session_state.user_name}!
            </h1>

            <p>
                Your MicroDegree learning journey starts here.
            </p>

            <div class="unlock-highlight">
                🔓 3 projects unlocked for you
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # PROJECTS
    # ========================================================

    st.markdown(
        """
        <div class="section-header">

            <h2>🔥 Your unlocked projects</h2>

            <p>
                Build practical experience by working on real-world projects.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    project1, project2, project3 = st.columns(3)

    with project1:

        st.markdown(
            """
            <div class="project-card">

                <div class="project-icon">
                    ☁️
                </div>

                <div class="project-level">
                    BEGINNER
                </div>

                <h3>
                    Cloud Foundations
                </h3>

                <p>
                    Understand cloud fundamentals,
                    core services, regions, storage,
                    networking and compute.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with project2:

        st.markdown(
            """
            <div class="project-card">

                <div class="project-icon">
                    🚀
                </div>

                <div class="project-level">
                    INTERMEDIATE
                </div>

                <h3>
                    Cloud Deployment
                </h3>

                <p>
                    Deploy an application to the cloud
                    and understand infrastructure,
                    configuration and deployment basics.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with project3:

        st.markdown(
            """
            <div class="project-card">

                <div class="project-icon">
                    💼
                </div>

                <div class="project-level">
                    ADVANCED
                </div>

                <h3>
                    Cloud Career Project
                </h3>

                <p>
                    Build a portfolio-ready practical
                    project that demonstrates your
                    cloud learning journey.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # VIDEO SECTION
    # ========================================================

    st.markdown(
        """
        <div class="section-header">

            <h2>🎬 Start learning today</h2>

            <p>
                Watch these videos to strengthen your cloud fundamentals.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    video_url = "https://www.youtube.com/watch?v=lfGoBcM5lZo"

    video1, video2, video3 = st.columns(3)

    with video1:

        st.markdown(
            """
            <div class="video-card">

                <div class="video-title">
                    ☁️ Cloud Fundamentals
                </div>

                <div class="video-description">
                    Start with the basics and understand
                    the fundamentals of cloud computing.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.video(video_url)

    with video2:

        st.markdown(
            """
            <div class="video-card">

                <div class="video-title">
                    🚀 Cloud Career
                </div>

                <div class="video-description">
                    Explore the skills and concepts needed
                    to begin your cloud career journey.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.video(video_url)

    with video3:

        st.markdown(
            """
            <div class="video-card">

                <div class="video-title">
                    🛠️ Build & Learn
                </div>

                <div class="video-description">
                    Learn by building practical projects
                    and applying your cloud knowledge.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.video(video_url)


    # ========================================================
    # PLAYLIST CTA
    # ========================================================

    playlist_url = (
        "https://www.youtube.com/playlist?"
        "list=PLQztdyH5OY4CdAveXCk83ZkugzNymb_9o"
    )

    st.markdown(
        f"""
        <div class="cta">

            <h2>
                ☁️ Want more Cloud learning?
            </h2>

            <p>
                Explore the complete Cloud Career Playlist
                and continue building your skills.
            </p>

            <a href="{playlist_url}" target="_blank">
                ▶ Watch Full Cloud Career Playlist
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # LEARNING STATS
    # ========================================================

    st.markdown(
        """
        <div class="section-header">

            <h2>📈 Your learning journey</h2>

            <p>
                Everything you need to keep moving forward.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    stat1, stat2, stat3 = st.columns(3)

    with stat1:

        st.markdown(
            """
            <div class="stat-card">

                <div class="stat-number">
                    3
                </div>

                <div class="stat-label">
                    PROJECTS UNLOCKED
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with stat2:

        st.markdown(
            f"""
            <div class="stat-card">

                <div class="stat-number">
                    {st.session_state.track}
                </div>

                <div class="stat-label">
                    SELECTED LEARNING TRACK
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with stat3:

        st.markdown(
            """
            <div class="stat-card">

                <div class="stat-number">
                    🚀
                </div>

                <div class="stat-label">
                    READY TO LEARN
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # START PROJECT BUTTON
    # ========================================================

    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button(
        "🔥 Start My First Project",
        use_container_width=True
    ):

        st.success(
            "Your first Cloud project is ready! 🚀 Let's start building."
        )


    # ========================================================
    # FOOTER
    # ========================================================

    st.markdown(
        """
        <div class="footer">

            © 2026 MicroDegree · Learn. Build. Grow. 🚀

        </div>
        """,
        unsafe_allow_html=True
    )