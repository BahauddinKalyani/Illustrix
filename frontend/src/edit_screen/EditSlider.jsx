import React from 'react';
import { useState } from 'react';
import { Button, Slider, Row, Col } from 'antd';
import ApiService from '../helpers/ApiService';

const EditSlider = (props) => {
  
    const [sliderValue, setSliderValue] = useState(50);
    

    const handleSettings = async (props, value, save, revert) => {
        let data = { ...props, 
            factor : value,
            save : save,
            revert : revert,
        }
        let imageUrl = await ApiService.handleSettings(data)
        props.updateImageToState(imageUrl)
    }
  
    const handleSliderChange = async (value) => {
        value = value/1000
        setSliderValue(value)
        handleSettings(props, value, 0, 0)
        // switch(props.slider_action) {
        //     case 'brightness':
        //         handleBrightness
        //         break;
        //     default:
        //         break;
        // }
    };
  
    const handleSave = async () => {
        handleSettings(props, sliderValue,1, 0)
        // switch(props.slider_action) {
        //     case 'brightness':
        //         handleBrightness
        //         break;
        //     default:
        //         break;
        // }
    };
  
    const handleRevert = async () => {
        handleSettings(props, sliderValue, 0, 1)
        // switch(props.slider_action) {
        //     case 'brightness':
        //         handleBrightness
        //         break;
        //     default:
        //         break;
        // }
    };

  return (
    props.show_slider &&
    <Row style={{ display: 'flex', alignItems: 'center', marginTop: '40px' }}>
        <Col span={6}></Col>
        <Col span={6}>
            <Slider min={1}
                max={5000} 
                defaultValue={1}
                onAfterChange={handleSliderChange}
            />
        </Col>
        <Col span={6}>
            <Button type="primary" style={{ marginLeft: 10 }} onClick={handleSave}>
                Save
            </Button>
            <Button style={{ marginLeft: 10 }} onClick={handleRevert}>
                Revert
            </Button>
        </Col>
    </Row>
  );
};

export default EditSlider;
