import 'antd/dist/reset.css';
import { Col, Row, ConfigProvider, message } from 'antd';
import ParticleBG from '../particle_bg/ParticleBG';
import SideBar from './SideBar/SideBar';
import InsideHeader from '../landing_header/InsideHeader';
import MainImage from './image/MainImage';
import UploadButton from './UploadButton';
import React, { Component } from 'react';
import ApiServiceHelper from '../helpers/ApiServiceHelper';
import UploadModal from '../modals/UploadModal';
import ApiService from '../helpers/ApiService'


const rowStyle = {
    textAlign: 'center',
    verticalAlign: 'center',
    width: '100%',
}

const config= {
    token: {
        colorPrimary: '#0E8388',
        colorBgBase: '#2C3333',
        colorText: '#CBE4DE',
        colorBorder: '#CBE4DE',
        colorIcon: '#CBE4DE',
        colorBgSpotlight: '#2C3333'
    },
};

const imageStyle = {
    width: "90vw",
    height: "100%",
}

class EditMain extends Component {
    constructor(props) {
        super(props);
        this.state = {
            imageUrl: null,
            backgroundImageUrl: null,
            jwtToken: this.props.location.state.jwt,
            is_updated: true,
            upload_modal_open: false,

            // jwtToken: localStorage.getItem('jwtToken')
        };
    }

    updateUploadModal(flag) {
        console.log(flag)
        this.setState({upload_modal_open: flag});
    }

    setImageUrl = async (imageUrl, background = false) => {
        const base64_image = await ApiServiceHelper.blobToBase64(imageUrl)
        const data = {
            image: base64_image
        }
        const header = {
            jwt_token: this.state.jwtToken
        }
        const response = await ApiServiceHelper.post('image/upload', data, header);
        if(background){
            this.updateBackgroundImageToState(response.url)
        } else {
            this.updateImageToState(response.url);
        }
        
        message.success(`file uploaded successfully`);
    };

    updateImageToState = (imageUrl) => {
        this.setState({ imageUrl: imageUrl, is_updated:  Math.random() });
    }

    updateBackgroundImageToState = async (imageUrl) => {
        this.setState({ backgroundImageUrl: imageUrl }, async function() {
            imageUrl = await ApiService.replaceBackground(this.state)
            this.updateImageToState(imageUrl)
        });
    }

    render() {
        return (
            <ConfigProvider 
                theme={config}
            >
                <ParticleBG />
                <UploadModal 
                    upload_modal_open={this.state.upload_modal_open} 
                    title="Upload Background" 
                    updateUploadModal={this.updateUploadModal.bind(this)} 
                    setImageUrl={this.setImageUrl.bind(this)} 
                />
                <InsideHeader />
                <Row style={rowStyle}>
                    <Col span={6}>
                        <SideBar 
                            jwtToken={this.state.jwtToken} 
                            imageUrl={this.state.imageUrl} 
                            backgroundImageUrl={this.state.backgroundImageUrl} 
                            updateImageToState={this.updateImageToState.bind(this)}
                            updateUploadModal={this.updateUploadModal.bind(this)} />
                    </Col>
                    <Col span={18} style={imageStyle}>
                        {/* <MainImage imageUrl="edit2.png" /> */}
                        {/* <UploadButton /> */}
                        {this.state.imageUrl ? (
                            <MainImage 
                                imageUrl={this.state.imageUrl} 
                                is_updated={this.state.is_updated}/>
                        ) : (
                            <UploadButton 
                                setImageUrl={this.setImageUrl.bind(this)}
                            />
                        )}
                    </Col>
                </Row>
            </ConfigProvider>
        );
    }
}

export default EditMain;
