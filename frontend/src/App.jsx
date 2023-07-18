import logo from './logo.svg';
import './App.css';
import 'antd/dist/reset.css';
import { Button, ConfigProvider, theme} from 'antd';
import { Layout, Space } from 'antd';
import LandingHeader from './landing_header/LandingHeader';
import LandingMain from './landing_main/LandingMain'
import ParticleBG from './particle_bg/ParticleBG'

const { Header, Footer, Sider, Content } = Layout;

const config: ThemeConfig = {
  token: {
    colorPrimary: '#0E8388',
    colorBgBase: '#2C3333',
    colorText: '#CBE4DE',
    colorBorder: '#CBE4DE',
    colorIcon: '#CBE4DE',
  },
};

const layoutStyel = {
  background: 'transparent',
}

function App() {
  return (
    <ConfigProvider 
    theme={config}
    >
      <Space direction="vertical" style={{ width: '100%' }} size={[0, 48]}>
        <Layout style={layoutStyel}>
          <LandingHeader ></LandingHeader>
          <LandingMain></LandingMain>
        </Layout>
      </Space>
    </ConfigProvider>
  );
}

export default App;
