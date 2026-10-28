import streamlit as st
from datetime import date, timedelta


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PetSphere",
    page_icon="🐾",
    layout="wide"
)


# ============================================================
# PET DATA
# ============================================================

pets = {

    "Bruno": {
        "type": "Dog",
        "breed": "Labrador Retriever",
        "age": 2,
        "gender": "Male",
        "location": "Hyderabad",
        "fee": 4500,
        "image": "https://images.unsplash.com/photo-1552053831-71594a27632d",
        "description": "Friendly and energetic Labrador who loves people and outdoor activities.",
        "vaccinated": True,
        "trained": True,
        "color": "Golden"
    },

    "Coco": {
        "type": "Cat",
        "breed": "Persian",
        "age": 1,
        "gender": "Female",
        "location": "Hyderabad",
        "fee": 3500,
        "image": "https://images.unsplash.com/photo-1574158622682-e40e69881006",
        "description": "Calm Persian cat who enjoys quiet environments and gentle attention.",
        "vaccinated": True,
        "trained": False,
        "color": "White"
    },

    "Max": {
        "type": "Dog",
        "breed": "Golden Retriever",
        "age": 3,
        "gender": "Male",
        "location": "Bengaluru",
        "fee": 5000,
        "image": "https://images.unsplash.com/photo-1558788353-f76d92427f16",
        "description": "Playful Golden Retriever with a friendly personality and excellent temperament.",
        "vaccinated": True,
        "trained": True,
        "color": "Golden"
    },

    "Milo": {
        "type": "Cat",
        "breed": "British Shorthair",
        "age": 2,
        "gender": "Male",
        "location": "Chennai",
        "fee": 4000,
        "image": "https://images.unsplash.com/photo-1533738363-b7f9aef128ce",
        "description": "Quiet and affectionate cat suitable for families and apartments.",
        "vaccinated": True,
        "trained": False,
        "color": "Grey"
    },

    "Bella": {
        "type": "Dog",
        "breed": "Beagle",
        "age": 1,
        "gender": "Female",
        "location": "Pune",
        "fee": 3000,
        "image": "https://images.unsplash.com/photo-1505628346881-b72b27e84530",
        "description": "Active Beagle who loves playing, walking and interacting with people.",
        "vaccinated": False,
        "trained": False,
        "color": "Brown"
    },

    "Luna": {
        "type": "Cat",
        "breed": "Siamese",
        "age": 3,
        "gender": "Female",
        "location": "Mumbai",
        "fee": 3800,
        "image": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131",
        "description": "Intelligent and social Siamese cat with a playful personality.",
        "vaccinated": True,
        "trained": True,
        "color": "Cream"
    }
}


# ============================================================
# SERVICE DATA
# ============================================================

services = {

    "🩺 Veterinary Consultation": {
        "price": 500,
        "duration": "30-45 minutes",
        "description": "General health consultation with a veterinarian."
    },

    "💉 Vaccination": {
        "price": 800,
        "duration": "20-30 minutes",
        "description": "Routine vaccination appointment."
    },

    "✂️ Grooming": {
        "price": 700,
        "duration": "1-2 hours",
        "description": "Bathing, trimming, nail care and basic grooming."
    },

    "🐕 Training": {
        "price": 1000,
        "duration": "1 hour",
        "description": "Basic obedience and behavioural training session."
    },

    "🏠 Pet Boarding": {
        "price": 900,
        "duration": "Per day",
        "description": "Safe temporary accommodation and basic pet care."
    },

    "🦷 Dental Cleaning": {
        "price": 1200,
        "duration": "45-60 minutes",
        "description": "Basic dental cleaning and oral health check."
    }
}


# ============================================================
# SESSION STATE
# ============================================================

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "adoption_request" not in st.session_state:
    st.session_state.adoption_request = None

if "adopted_pet" not in st.session_state:
    st.session_state.adopted_pet = None

if "service_history" not in st.session_state:
    st.session_state.service_history = []

if "service_booking" not in st.session_state:
    st.session_state.service_booking = None


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🐾 PetSphere")

st.sidebar.caption(
    "Pet Adoption & Complete Pet Care"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🐾 Explore Pets",
        "❤️ Favorites",
        "🏠 Adoption",
        "🩺 Pet Services",
        "💉 Health Tracker",
        "💰 Pet Cost Planner",
        "🐶 My Pet"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "PetSphere is a demonstration application. "
    "Pet information, prices and services are sample data."
)


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.title("🐾 PetSphere")

    st.subheader(
        "Find a companion. Care for them. Keep them healthy. ❤️"
    )

    st.divider()

    col1, col2 = st.columns([1.2, 1])

    with col1:

        st.image(
            "https://images.unsplash.com/photo-1450778869180-41d0601e046e",
            use_container_width=True
        )

    with col2:

        st.markdown("## Welcome to PetSphere 🐾")

        st.write(
            """
            PetSphere is a complete pet adoption and care
            platform that helps users explore pets, submit
            adoption requests and manage their pet's
            ongoing care.
            """
        )

        st.success(
            "🐶 Find your companion and give them a happy home."
        )

    st.divider()

    st.header("✨ What can you do?")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Available Pets",
            len(pets)
        )

    with col2:

        st.metric(
            "Pet Services",
            len(services)
        )

    with col3:

        st.metric(
            "Pet Types",
            "Dogs & Cats"
        )

    with col4:

        st.metric(
            "Care Categories",
            "6"
        )

    st.divider()

    st.header("🌟 Popular Pets")

    popular_names = list(pets.keys())[:3]

    cols = st.columns(3)

    for i, pet_name in enumerate(popular_names):

        pet = pets[pet_name]

        with cols[i]:

            st.image(
                pet["image"],
                use_container_width=True
            )

            st.subheader(
                f"🐾 {pet_name}"
            )

            st.write(
                f"{pet['breed']} • {pet['age']} years"
            )

            st.write(
                f"📍 {pet['location']}"
            )


# ============================================================
# EXPLORE PETS
# ============================================================

elif page == "🐾 Explore Pets":

    st.title("🐾 Explore Pets")

    st.write(
        "Find a pet based on your preferences."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        selected_type = st.selectbox(
            "Pet Type",
            [
                "All",
                "Dog",
                "Cat"
            ]
        )

    with col2:

        selected_gender = st.selectbox(
            "Gender",
            [
                "All",
                "Male",
                "Female"
            ]
        )

    with col3:

        selected_location = st.selectbox(
    "Location",
    ["All"] + sorted(
        list(
            set(
                pet["location"]
                for pet in pets.values()
            )
        )
    )
)

    st.divider()

    filtered_pets = {}

    for name, pet in pets.items():

        type_match = (
            selected_type == "All"
            or pet["type"] == selected_type
        )

        gender_match = (
            selected_gender == "All"
            or pet["gender"] == selected_gender
        )

        location_match = (
            selected_location == "All"
            or pet["location"] == selected_location
        )

        if (
            type_match
            and gender_match
            and location_match
        ):

            filtered_pets[name] = pet

    if len(filtered_pets) == 0:

        st.warning(
            "No pets match your selected filters."
        )

    else:

        st.success(
            f"{len(filtered_pets)} pet(s) found."
        )

        pet_names = list(filtered_pets.keys())

        for start in range(
            0,
            len(pet_names),
            3
        ):

            row = pet_names[
                start:start + 3
            ]

            cols = st.columns(3)

            for i, name in enumerate(row):

                pet = filtered_pets[name]

                with cols[i]:

                    st.image(
                        pet["image"],
                        use_container_width=True
                    )

                    st.subheader(
                        f"🐾 {name}"
                    )

                    st.write(
                        f"**Breed:** {pet['breed']}"
                    )

                    st.write(
                        f"**Age:** {pet['age']} years"
                    )

                    st.write(
                        f"**Gender:** {pet['gender']}"
                    )

                    st.write(
                        f"📍 {pet['location']}"
                    )

                    st.write(
                        f"💰 Adoption Fee: ₹{pet['fee']:,}"
                    )

                    if st.button(
                        "View Profile",
                        key=f"profile_{name}"
                    ):

                        st.session_state.selected_pet = name

            st.divider()

        if "selected_pet" in st.session_state:

            name = st.session_state.selected_pet
            pet = pets[name]

            st.header(
                f"🐾 {name}'s Profile"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.image(
                    pet["image"],
                    use_container_width=True
                )

            with col2:

                st.subheader(
                    f"{name} — {pet['breed']}"
                )

                st.write(
                    pet["description"]
                )

                st.write(
                    f"🐾 **Type:** {pet['type']}"
                )

                st.write(
                    f"🎂 **Age:** {pet['age']} years"
                )

                st.write(
                    f"⚥ **Gender:** {pet['gender']}"
                )

                st.write(
                    f"🎨 **Color:** {pet['color']}"
                )

                st.write(
                    f"📍 **Location:** {pet['location']}"
                )

                st.write(
                    f"💉 **Vaccinated:** "
                    f"{'Yes' if pet['vaccinated'] else 'No'}"
                )

                st.write(
                    f"🐕 **Trained:** "
                    f"{'Yes' if pet['trained'] else 'No'}"
                )

                st.write(
                    f"💰 **Adoption Fee:** "
                    f"₹{pet['fee']:,}"
                )

                if name not in st.session_state.favorites:

                    if st.button(
                        "❤️ Add to Favorites",
                        key=f"fav_{name}"
                    ):

                        st.session_state.favorites.append(
                            name
                        )

                        st.success(
                            f"{name} added to favorites."
                        )

                else:

                    st.success(
                        "❤️ Added to Favorites"
                    )

                if st.button(
                    "🏠 Adopt This Pet",
                    key=f"adopt_{name}"
                ):

                    st.session_state.adoption_request = name

                    st.success(
                        f"Adoption process started for {name}."
                    )


# ============================================================
# FAVORITES
# ============================================================

elif page == "❤️ Favorites":

    st.title("❤️ My Favorite Pets")

    if len(st.session_state.favorites) == 0:

        st.info(
            "You haven't added any pets to favorites."
        )

    else:

        for name in st.session_state.favorites:

            pet = pets[name]

            col1, col2 = st.columns([1, 2])

            with col1:

                st.image(
                    pet["image"],
                    use_container_width=True
                )

            with col2:

                st.subheader(
                    f"🐾 {name}"
                )

                st.write(
                    f"{pet['breed']} • {pet['age']} years"
                )

                st.write(
                    pet["description"]
                )

                if st.button(
                    "Remove",
                    key=f"remove_{name}"
                ):

                    st.session_state.favorites.remove(
                        name
                    )

                    st.rerun()

            st.divider()


# ============================================================
# ADOPTION
# ============================================================

elif page == "🏠 Adoption":

    st.title("🏠 Pet Adoption")

    if st.session_state.adoption_request is None:

        st.info(
            "Go to Explore Pets and select "
            "a pet to start an adoption request."
        )

    else:

        name = st.session_state.adoption_request
        pet = pets[name]

        st.header(
            f"🐾 Adoption Request — {name}"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.image(
                pet["image"],
                use_container_width=True
            )

        with col2:

            st.write(
                f"**Breed:** {pet['breed']}"
            )

            st.write(
                f"**Age:** {pet['age']} years"
            )

            st.write(
                f"**Location:** {pet['location']}"
            )

            st.write(
                f"**Adoption Fee:** ₹{pet['fee']:,}"
            )

        st.divider()

        with st.form("adoption_form"):

            st.subheader(
                "👤 Adopter Information"
            )

            name_input = st.text_input(
                "Full Name"
            )

            email = st.text_input(
                "Email"
            )

            phone = st.text_input(
                "Phone Number"
            )

            address = st.text_area(
                "Address"
            )

            home_type = st.selectbox(
                "Type of Home",
                [
                    "Apartment",
                    "Independent House",
                    "Farm House"
                ]
            )

            experience = st.selectbox(
                "Previous Pet Experience",
                [
                    "First-time pet owner",
                    "Have owned pets before"
                ]
            )

            terms = st.checkbox(
                "I confirm that the information provided is correct."
            )

            submit = st.form_submit_button(
                "🏠 Submit Adoption Request"
            )

        if submit:

            if name_input == "":
                st.error(
                    "Please enter your name."
                )

            elif email == "":
                st.error(
                    "Please enter your email."
                )

            elif phone == "":
                st.error(
                    "Please enter your phone number."
                )

            elif not terms:
                st.error(
                    "Please confirm the information."
                )

            else:

                adoption_fee = pet["fee"]

                processing_fee = 250

                total = (
                    adoption_fee
                    + processing_fee
                )

                st.session_state.adopted_pet = name

                st.success(
                    "🎉 Adoption request submitted successfully!"
                )

                st.divider()

                st.subheader(
                    "🧾 Adoption Summary"
                )

                st.write(
                    f"**Adopter:** {name_input}"
                )

                st.write(
                    f"**Pet:** {name}"
                )

                st.write(
                    f"**Breed:** {pet['breed']}"
                )

                st.write(
                    f"**Home Type:** {home_type}"
                )

                st.write(
                    f"**Pet Experience:** {experience}"
                )

                st.write(
                    f"**Adoption Fee:** ₹{adoption_fee:,}"
                )

                st.write(
                    f"**Processing Fee:** ₹{processing_fee:,}"
                )

                st.write(
                    f"**Total:** ₹{total:,}"
                )

                st.info(
                    "This is a demonstration adoption system. "
                    "The payment is not processed."
                )


# ============================================================
# PET SERVICES
# ============================================================

elif page == "🩺 Pet Services":

    st.title("🩺 Pet Services")

    if st.session_state.adopted_pet is not None:

        selected_pet = st.session_state.adopted_pet

        st.success(
            f"🐾 Selected Pet: {selected_pet}"
        )

    else:

        selected_pet = st.selectbox(
            "Select Pet",
            list(pets.keys())
        )

    st.divider()

    selected_service = st.selectbox(
        "Choose a Service",
        list(services.keys())
    )

    service = services[selected_service]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Estimated Cost",
            f"₹{service['price']:,}"
        )

    with col2:

        st.metric(
            "Duration",
            service["duration"]
        )

    with col3:

        st.metric(
            "Pet",
            selected_pet
        )

    st.write(
        service["description"]
    )

    st.divider()

    st.subheader(
        "📅 Schedule Service"
    )

    service_date = st.date_input(
        "Service Date",
        min_value=date.today()
    )

    service_time = st.selectbox(
        "Preferred Time",
        [
            "09:00 AM",
            "11:00 AM",
            "01:00 PM",
            "03:00 PM",
            "05:00 PM"
        ]
    )

    service_center = st.selectbox(
        "Service Center",
        [
            "PetSphere Care Center - Hyderabad",
            "PetSphere Care Center - Bengaluru",
            "PetSphere Care Center - Chennai"
        ]
    )

    notes = st.text_area(
        "Additional Requirements"
    )

    if st.button(
        "🔧 Book Service"
    ):

        booking = {
            "pet": selected_pet,
            "service": selected_service,
            "date": service_date,
            "time": service_time,
            "center": service_center,
            "cost": service["price"],
            "notes": notes
        }

        st.session_state.service_booking = booking

        st.session_state.service_history.append(
            booking
        )

        st.success(
            "🎉 Service appointment booked successfully!"
        )

    if st.session_state.service_booking is not None:

        booking = st.session_state.service_booking

        st.divider()

        st.subheader(
            "📋 Appointment Summary"
        )

        st.write(
            f"🐾 **Pet:** {booking['pet']}"
        )

        st.write(
            f"🔧 **Service:** {booking['service']}"
        )

        st.write(
            f"📅 **Date:** {booking['date']}"
        )

        st.write(
            f"⏰ **Time:** {booking['time']}"
        )

        st.write(
            f"📍 **Center:** {booking['center']}"
        )

        st.write(
            f"💰 **Estimated Cost:** ₹{booking['cost']:,}"
        )


# ============================================================
# HEALTH TRACKER
# ============================================================

elif page == "💉 Health Tracker":

    st.title("💉 Pet Health Tracker")

    selected_pet = st.selectbox(
        "Select Pet",
        list(pets.keys())
    )

    pet = pets[selected_pet]

    st.header(
        f"🐾 {selected_pet}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        if pet["vaccinated"]:

            st.success(
                "💉 Vaccination\n\nUp to date"
            )

        else:

            st.warning(
                "💉 Vaccination\n\nDue"
            )

    with col2:

        if pet["trained"]:

            st.success(
                "🐕 Training\n\nCompleted"
            )

        else:

            st.info(
                "🐕 Training\n\nNot completed"
            )

    with col3:

        st.info(
            "🩺 Health Check\n\nSchedule regularly"
        )

    st.divider()

    st.subheader(
        "💉 Vaccination Schedule"
    )

    vaccinations = [
        ("Rabies", True),
        ("DHPP", True),
        ("Booster", False),
        ("Annual Check", False)
    ]

    for vaccine, completed in vaccinations:

        if completed:

            st.write(
                f"✅ {vaccine}"
            )

        else:

            st.write(
                f"⚠️ {vaccine} — Due Soon"
            )

    st.divider()

    st.subheader(
        "📅 Next Health Check"
    )

    next_check = date.today() + timedelta(
        days=30
    )

    st.info(
        f"Next recommended check: {next_check}"
    )


# ============================================================
# PET COST PLANNER
# ============================================================

elif page == "💰 Pet Cost Planner":

    st.title("💰 Pet Cost Planner")

    st.write(
        "Estimate the monthly cost of caring for a pet."
    )

    col1, col2 = st.columns(2)

    with col1:

        food = st.number_input(
            "🍖 Food per Month",
            min_value=0,
            value=2500,
            step=100
        )

        grooming = st.number_input(
            "✂️ Grooming per Month",
            min_value=0,
            value=700,
            step=100
        )

        medical = st.number_input(
            "🩺 Medical / Month",
            min_value=0,
            value=500,
            step=100
        )

    with col2:

        accessories = st.number_input(
            "🧸 Accessories / Month",
            min_value=0,
            value=300,
            step=100
        )

        training = st.number_input(
            "🐕 Training / Month",
            min_value=0,
            value=500,
            step=100
        )

        other = st.number_input(
            "📦 Other Expenses",
            min_value=0,
            value=300,
            step=100
        )

    if st.button(
        "🧮 Calculate Pet Cost"
    ):

        monthly = (
            food
            + grooming
            + medical
            + accessories
            + training
            + other
        )

        yearly = monthly * 12

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Monthly Cost",
                f"₹{monthly:,}"
            )

        with col2:

            st.metric(
                "Yearly Cost",
                f"₹{yearly:,}"
            )

        st.divider()

        st.subheader(
            "📊 Expense Breakdown"
        )

        expenses = {
            "Food": food,
            "Grooming": grooming,
            "Medical": medical,
            "Accessories": accessories,
            "Training": training,
            "Other": other
        }

        for item, amount in expenses.items():

            st.write(
                f"**{item}:** ₹{amount:,}"
            )

            st.progress(
                amount / monthly
                if monthly > 0
                else 0
            )


# ============================================================
# MY PET
# ============================================================

elif page == "🐶 My Pet":

    st.title("🐶 My Pet Dashboard")

    if st.session_state.adopted_pet is None:

        st.info(
            "You haven't adopted a pet through PetSphere yet."
        )

        st.write(
            "You can still use PetSphere services by "
            "selecting a pet manually."
        )

    else:

        name = st.session_state.adopted_pet
        pet = pets[name]

        st.header(
            f"🐾 {name}"
        )

        col1, col2 = st.columns([1, 2])

        with col1:

            st.image(
                pet["image"],
                use_container_width=True
            )

        with col2:

            st.subheader(
                pet["breed"]
            )

            st.write(
                f"🎂 Age: {pet['age']} years"
            )

            st.write(
                f"⚥ Gender: {pet['gender']}"
            )

            st.write(
                f"📍 Location: {pet['location']}"
            )

            st.write(
                f"💉 Vaccinated: "
                f"{'Yes' if pet['vaccinated'] else 'No'}"
            )

            st.write(
                f"🐕 Trained: "
                f"{'Yes' if pet['trained'] else 'No'}"
            )

        st.divider()

        st.subheader(
            "📋 Recent Service History"
        )

        pet_history = [
            item
            for item in st.session_state.service_history
            if item["pet"] == name
        ]

        if len(pet_history) == 0:

            st.info(
                "No service history yet."
            )

        else:

            for item in pet_history:

                st.write(
                    f"📅 {item['date']} — "
                    f"{item['service']} — "
                    f"₹{item['cost']:,}"
                )

        st.divider()

        st.subheader(
            "❤️ Pet Care Overview"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.success(
                "💉 Vaccination\n\n"
                + (
                    "Up to date"
                    if pet["vaccinated"]
                    else "Due"
                )
            )

        with col2:

            st.info(
                "✂️ Grooming\n\n"
                "Recommended monthly"
            )

        with col3:

            st.warning(
                "🩺 Health Check\n\n"
                "Next check recommended"
            )