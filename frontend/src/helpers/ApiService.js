import ApiServiceHelper from './ApiServiceHelper';

// const API_BASE_URL = 'http://localhost:8000';

const ApiService = {

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

    handleAction: async (props) => {
        console.log(props)
        const data = {
            image_url: props.imageUrl,
        }
        const header = {
            jwt_token: props.jwtToken
        }
        const response = await ApiServiceHelper.post('image/'+props.api_url, data, header);
        console.log(response)
        return response.url
    },

    handleSettings: async (props) => {
        console.log(props)
        const data = {
            image_url: props.imageUrl,
            factor: props.factor,
            save: props.save,
            revert: props.revert,
        }
        const header = {
            jwt_token: props.jwtToken
        }
        const response = await ApiServiceHelper.post('image/'+props.slider_action, data, header);
        console.log(response)
        return response.url
    },

    getAllImages: async (props) => {
        console.log(props)
        const header = {
            jwt_token: props.jwtToken
        }
        const response = await ApiServiceHelper.get('image/get_user_images', header);
        console.log(response)
        return response.url
    }
};

export default ApiService;