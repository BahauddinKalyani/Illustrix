import 'antd/dist/reset.css';
import './sidebar.css'
import React from 'react';
import { Menu, MenuProps } from 'antd';
import {
    AppstoreOutlined,
    MailOutlined,
    SettingOutlined,
} from '@ant-design/icons';
import ApiService from '../../helpers/ApiService';

type MenuItem = Required<MenuProps>['items'][number];

const items:  MenuItem[]  = [
    getItem('Background', 'sub1', <MailOutlined />, [
        getItem('Background Remove', '1'),
        getItem('Blur Background', '2'),
        getItem('Replace Background', '3'),
        // getItem('Reset Background', '4'),
    ]),
    getItem('Enhancements', 'sub2', <AppstoreOutlined />, [
        getItem('Image Super Resolutions', '5'),
    ]),
    getItem('Transformations', 'sub3', <SettingOutlined />, [
        getItem('Cartoon', '6'),
        getItem('Sketch', '7'),
        getItem('Black & White', '8'),
    ]),
    getItem('Adjustments', 'sub4', <SettingOutlined />, [
        getItem('Change Brightness', '9'),
        getItem('Adjust Contrast', '10'),
        getItem('Change Hue', '11'),
        getItem('Change Saturation', '12'),
        getItem('Flip Image', '13'),
        getItem('Adjust Sharpness', '14'),
    ]),
    getItem('File', 'sub5', <SettingOutlined />, [
        getItem('Save Image', '15'),
        getItem('Delete Image', '16'),
    ]),
];

function getItem(
    label: React.ReactNode,
    key: React.Key,
    icon?: React.ReactNode,
    children?: MenuItem[],
    type?: 'group',
): MenuItem {
    return {
      key,
      icon,
      children,
      label,
      type,
    };
}

const rootSubmenuKeys = ['sub1', 'sub2', 'sub4'];

class SideBar extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
          openKeys: ['sub1'],
        };
    }

    setOpenKeys(keys) {
      this.setState({
        openKeys: keys,
      });
    }

    onOpenChange(keys) {
      console.log(keys)
      const latestOpenKey = keys.find((key) => this.state.openKeys.indexOf(key) === -1);
      if (rootSubmenuKeys.indexOf(latestOpenKey) === -1) {
        this.setOpenKeys(keys);
      } else {
        this.setOpenKeys(latestOpenKey ? [latestOpenKey] : []);
      }
      console.log(keys)
        
    }

    async handleClick(data){
        console.log(data)
        let imageUrl = ''
        switch(data.key) {
            case '1':
                imageUrl = await ApiService.removeBackground(this.props)
                this.props.updateImageToState(imageUrl)
                break;
            case '2':
                imageUrl = await ApiService.blurrBackground(this.props)
                this.props.updateImageToState(imageUrl)
                break;
            case '3':
                // imageUrl = await ApiService.blackAndWhite(this.props)
                // this.props.updateImageToState(imageUrl)
                this.props.updateUploadModal(true)
                break;
            case '8':
                imageUrl = await ApiService.blackAndWhite(this.props)
                this.props.updateImageToState(imageUrl)
                break;
            default:
                break;
        }
    }

    render() {
        return (
            <div style={{ width: 256, marginTop: 15}}>
                <Menu
                    mode="inline"
                    theme="dark"
                    items={items}
                    openKeys={this.state.openKeys}
                    onClick={this.handleClick.bind(this)}
                    onOpenChange={this.onOpenChange.bind(this)}
                />
            </div>
        )
    }
}

export default SideBar;