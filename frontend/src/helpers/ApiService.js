import axios from 'axios';
import ApiServiceHelper from './ApiServiceHelper';

// const API_BASE_URL = 'http://localhost:8000';

const ApiService = {
    removeBackground: async (props) => {
        console.log(props)
        const data = {
            image_url: props.imageUrl
        }
        const header = {
            jwt_token: props.jwtToken
        }
        const response = await ApiServiceHelper.post('image/background_remove', data, header);
        console.log(response)
        return response.url
    },
    
    blurrBackground: async (props) => {
        console.log(props)
        const data = {
            image_url: props.imageUrl
        }
        const header = {
            jwt_token: props.jwtToken
        }
        const response = await ApiServiceHelper.post('image/background_blur', data, header);
        console.log(response)
        return response.url
    },

    replaceBackground: async (props) => {
        console.log(props)
        const data = {
            image_url: props.imageUrl,
            background_url: props.backgroundImageUrl
        }
        const header = {
            jwt_token: props.jwtToken
        }
        const response = await ApiServiceHelper.post('image/background_replace', data, header);
        console.log(response)
        return response.url
    },

    blackAndWhite: async (props) => {
        console.log(props)
        const data = {
            image_url: props.imageUrl
        }
        const header = {
            jwt_token: props.jwtToken
        }
        const response = await ApiServiceHelper.post('image/black_and_white', data, header);
        console.log(response)
        return response.url
    },
};

export default ApiService;