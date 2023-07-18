import { Layout } from 'antd';
import { Button, ConfigProvider, theme} from 'antd';

const { Header } = Layout;

const headerStyle = {
    background: 'transparent',
}

const buttonStyle = {
    margin: '30px 15px',
    float: 'right',
}

const imageStyle = {
    margin: '30px 15px',
    height: '50px',
    width: '100px',
}

function LandingHeader() {
    return (
        <Header style={headerStyle}>
            <img style={imageStyle} src='logo-clr-sm.png' alt='logo'></img>
            {/* <Button style={buttonStyle} type='deafult'>Sign up</Button> */}
            <Button style={buttonStyle} type='deafult'>Contact us</Button>
            <Button style={buttonStyle} type='deafult'>Documents</Button>
            <Button style={buttonStyle} type='deafult'>Pricing</Button>
            <Button style={buttonStyle} type='deafult'>Home</Button>
            {/* <Button style={buttonStyle} type='primary'>Login</Button> */}
        </Header>  
    );
}
  
export default LandingHeader;